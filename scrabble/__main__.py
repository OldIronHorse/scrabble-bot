import time
from collections import namedtuple
from itertools import cycle, permutations
from functools import reduce
from scrabble.tiles import shake, new_bag
from scrabble.board import new_board, add_horizontal
from scrabble.checker import scowl_35
from scrabble.scorer import score_move

#TODO: wordtree as alternative to brute force
#TODO: blank tile support

def basic(game, player):
  if game['board'] == new_board():
    # first move
    print(player)
    candidate_words = {word for word in {''.join(w) for w in reduce(lambda acc, l: acc + list(l), (permutations(player['tiles'], n) for n in range(2, len(player['tiles']) + 1)), [])} if word in scowl_35()}
    print(candidate_words)
    candidate_moves = [(word, board, score_move(game['board'], board)) 
                        for word, board in
                        [(word, add_horizontal(game['board'], 
                                               (7, 8 - len(word)), 
                                               word))
                         for word in candidate_words]]
    word, board, score  = \
      reduce(lambda best, move: move if move[2] > best[2] else best,
             candidate_moves)
    print(word, score)
    game['board'] = board
    tiles = list(player['tiles'])
    for l in word:
      tiles.remove(l)
    player['tiles'] = ''.join(tiles)

def print_board(board):
  for row in board:
    print(row)

def print_player(player):
  print('player', player['name'], '[', player['score'], ']: ', player['tiles'])

def draw(game, player):
  game['bag'] = game['bag'][7 - len(player['tiles']):]
  player['tiles'] = player['tiles'] \
      + game['bag'][:(7 - len(player['tiles']))]

game = {
  'bag': shake(new_bag()), 
  'board': new_board(), 
}

players = [{
    'name': 'Player1',
    'tiles': '',
    'score': 0,
    'strategy': basic
  },{
    'name': 'Player2',
    'tiles': '',
    'score': 0,
    'strategy': basic
  },
]

for player in cycle(players):
  print_board(game['board'])
  game['bag'] = shake(game['bag'])
  draw(game, player)
  print_player(player)
  start = time.time()
  player['strategy'](game, player)
  print(time.time() - start)
  ##TODO: check new board is valid?
  print_board(game['board'])
  input('Press Enter to continue...')

