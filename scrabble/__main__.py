from collections import namedtuple
from itertools import cycle
from scrabble.tiles import shake, new_bag
from scrabble.board import new_board

def print_board(board):
  for row in board:
    print(row)

def draw(game, player):
  game['bag'] = game['bag'][7 - len(game['players'][player]['tiles']):]
  game['players'][player]['tiles'] = game['players'][player]['tiles'] \
      + game['bag'][:(7 - len(game['players'][player]['tiles']))]

game = {
  'bag': shake(new_bag()), 
  'board': new_board(), 
  'players': [{
      'tiles': '',
      'score': 0,
    },{
      'tiles': '',
      'score': 0,
    },
  ]
}

for player in cycle([0, 1]):
  print_board(game['board'])
  draw(game, player)
  print('player', player, 
        '[', game['players'][player]['score'], ']: ', 
        game['players'][player]['tiles'])
  input('Press Enter to continue...')

