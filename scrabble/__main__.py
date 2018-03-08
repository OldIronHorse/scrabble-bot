import time
from itertools import cycle
from scrabble.board import new_board, add_horizontal, add_vertical
from scrabble.scorer import score_move
from scrabble.tiles import shake, new_bag
from scrabble.strategies import basic
from scrabble.checker import scowl_35, is_valid_arrangement, get_words

def print_board(board):
  for row in board:
    print(row)

def print_player(player):
  print('{} [{}] {:.6f}s {}'.format(player['name'], player['score'], 
      player['time'], player['tiles']))

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
    'strategy': basic,
    'time': 0,
  },{
    'name': 'Player2',
    'tiles': '',
    'score': 0,
    'strategy': basic,
    'time': 0,
  },
]

def update_game_player(game, player, board, word):
  if not is_valid_arrangement(board) \
      or not get_words(board).issubset(scowl_35()):
    raise InvalidMoveError
  player['score'] += score_move(game['board'], board)
  game['board'] = board
  tiles = list(player['tiles'])
  for l in word:
    tiles.remove(l)
  player['tiles'] = ''.join(tiles)

def action_add_horizontal(game, player, params):
  start, word = params
  board = add_horizontal(game['board'], start, word)
  update_game_player(game, player, board, word)

def action_add_vertical(game, player, params):
  start, word = params
  board = add_vertical(game['board'], start, word)
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
  print_board(game['board'])
  draw(game, player)
  print_player(player)
  start = time.time()
  action, params = player['strategy'](game['board'], player['tiles'])
  action_history.append(action)
  player['time'] += time.time() - start
  print(action, params)
  actions[action](game, player, params)
  print_board(game['board'])
  print_player(player)
  print('bag:', ''.join(sorted(game['bag'])))
  #input('Press Enter to continue...')
  if action_history[len(action_history) - 3:] == \
      ['exchange_tiles', 'exchange_tiles', 'exchange_tiles'] \
      or (not game['bag'] and not player['tiles']):
    for player in players:
      print_player(player)
    break;

