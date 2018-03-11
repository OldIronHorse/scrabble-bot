import time
from itertools import cycle
from functools import partial
from word_tree import make_word_tree
from scrabble.board import new_board, add_horizontal, add_vertical
from scrabble.scorer import score_move, score_word
from scrabble.tiles import shake, new_bag
from scrabble.strategies import whole_words, longest_first, shortest_first, \
  shape_first
from scrabble.checker import scowl, is_valid_arrangement, get_words

def print_board(board):
  for row in board:
    print(row)

def print_player(player):
  print('{} {} [{}] {:.6f}s {}'.format(player['name'], len(player['words']),
        player['score'], player['time'], player['tiles']))

def draw(game, player):
  game['bag'] = shake(game['bag'])
  to_draw = 7 - len(player['tiles'])
  drawn_tiles = game['bag'][:to_draw]
  game['bag'] = game['bag'][to_draw:]
  player['tiles'] = player['tiles'] + drawn_tiles

game = {
  'bag': shake(new_bag()), 
  'board': new_board(), 
}

players = [{
    'name': 'Player1',
    'tiles': '',
    'score': 0,
    'strategy': partial(shape_first, scowl(35), make_word_tree(scowl(35))),
    'time': 0,
    'words': [],
  },{
    'name': 'Player2',
    'tiles': '',
    'score': 0,
    'strategy': partial(whole_words, scowl(35)),
    'time': 0,
    'words': [],
  },{
    'name': 'Player3',
    'tiles': '',
    'score': 0,
    'strategy': partial(shape_first, scowl(35), make_word_tree(scowl(35))),
    'time': 0,
    'words': [],
  },{
    'name': 'Player4',
    'tiles': '',
    'score': 0,
    'strategy': partial(shortest_first, scowl(35)),
    'time': 0,
    'words': [],
  },
]

def update_game_player(game, player, board, word):
  if not is_valid_arrangement(board) \
      or not get_words(board).issubset(scowl(80)):
    raise InvalidMoveError
  player['score'] += score_move(game['board'], board)
  game['board'] = board
  tiles = list(player['tiles'])
  for l in word:
    tiles.remove(l)
  player['tiles'] = ''.join(tiles)
  player['words'].append(word)

def action_add_horizontal(game, player, params):
  start, word = params
  board = add_horizontal(game['board'], start, word)
  print('move score:', score_move(game['board'], board))
  update_game_player(game, player, board, word)

def action_add_vertical(game, player, params):
  start, word = params
  board = add_vertical(game['board'], start, word)
  print('move score:', score_move(game['board'], board))
  update_game_player(game, player, board, word)

def action_exchange_tiles(game, player, tiles):
  player_tiles = list(player['tiles'])
  for l in tiles:
    player_tiles.remove(l)
  player['tiles'] = ''.join(player_tiles)
  game['bag'] = game['bag'] + tiles
  draw(game, player)

actions = {
  'add_horizontal': action_add_horizontal,
  'add_vertical': action_add_vertical,
  'exchange_tiles': action_exchange_tiles,
}

action_history = []

for player in cycle(players):
  draw(game, player)
  print_player(player)
  start = time.time()
  action, params = player['strategy'](game['board'], player['tiles'])
  action_history.append(action)
  player['time'] += time.time() - start
  print(action, params)
  actions[action](game, player, params)
  print_board(game['board'])
  print('bag:', ''.join(sorted(game['bag'])))
  #input('Press Enter to continue...')
  if action_history[len(action_history) - (2 * len(players)):] == \
      ['exchange_tiles'] * 2 * len(players) \
      or (not game['bag'] and not player['tiles']):
    for player in players:
      player['score'] -= score_word(player['tiles'])
      print_player(player)
      print(player['words'])
    print(get_words(game['board']))
    break;

