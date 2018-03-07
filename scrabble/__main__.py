import time
from itertools import cycle
from scrabble.board import new_board
from scrabble.tiles import shake, new_bag
from scrabble.strategies import basic

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

