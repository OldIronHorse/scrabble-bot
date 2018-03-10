from scrabble import InvalidTilePlacementError

empty_board = tuple('               ' for i in range (0, 15))

def new_board():
  return empty_board

def add_horizontal(board, start, word):
  try:
    r, c = start
    new_row = board[r][:c]
    for l in word:
      while board[r][c] != ' ':
        new_row += board[r][c]
        c += 1
      new_row += l
      c += 1
    new_row += board[r][c:] 
    if len(new_row) > 15:
      raise InvalidTilePlacementError
    return board[:r] + (new_row,) + board[r + 1:]
  except IndexError:
    raise InvalidTilePlacementError

def transpose(board):
  return tuple(map(lambda row: ''.join(row), zip(*board)))

def add_vertical(board, start, word):
  r, c = start
  return transpose(add_horizontal(transpose(board), (c, r), word))
