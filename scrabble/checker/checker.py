from functools import reduce
from scrabble.board import new_board

def words(lines):
  return {w for w 
            in reduce(lambda r1, r2: r1 + r2, 
                      [r.split(' ') for r in lines]) 
            if len(w) > 1}

def get_words(board):
  cols = []
  for col in range(0, 15):
    column = []
    for row in range(0, 15):
      column.append(board[row][col])
    cols.append(''.join(column))
  return words(board) | words(cols)

#TODO: refactor to validate board + move ((r,c), word
def is_valid_arrangement(board):
  if board == new_board():
    return True
  if board[7][7] == ' ':
    return False
  #TODO: check contiguous
  return True
