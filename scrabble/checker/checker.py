from functools import reduce
from scrabble.board import new_board

def words(lines):
  return {w for w 
            in reduce(lambda r1, r2: r1 + r2, 
                      [r.split(' ') for r in lines]) 
            if len(w) > 1}

def get_words(board):
  return words(board) | words(list(map(lambda line: ''.join(line),zip(*board))))

#TODO: refactor to validate board + move ((r,c), word
def is_valid_arrangement(board):
  if board == new_board():
    return True
  if board[7][7] == ' ':
    return False
  tiles = set()
  for row in range(0,15):
    for col in range(0,15):
      if board[row][col] != ' ':
        tiles.add((row, col))
  check_contiguous((7,7), tiles)
  return not tiles

def check_contiguous(tile, tiles):
  tiles.remove(tile)
  row, col = tile
  for t in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col -1)]:
    if t in tiles:
      check_contiguous(t, tiles)
