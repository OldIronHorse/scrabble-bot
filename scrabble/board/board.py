from scrabble import InvalidTilePlacementError

empty_board = tuple('               ' for i in range (0, 15))

def new_board():
  return empty_board

def add_horizontal(board, start, word):
  row_index, col_index = start
  row = board[row_index]
  word_as_row = ''.join([' ' for i in range(0, col_index)] \
                        + [word] \
                        + [' ' for i in range(col_index + len(word), 15)])
  if len(word_as_row) > 15:
    raise InvalidTilePlacementError
  new_row = ''
  for r,w in zip(row, word_as_row):
    if w == ' ':
      new_row += r
    elif r == ' ':
      new_row += w
    else:
      raise InvalidTilePlacementError
  return board[:row_index] + (new_row,) + board[row_index + 1:]

def add_vertical(board, start, word):
  row_index, col_index = start
  word_as_col = ''.join([' ' for i in range(0, row_index)] \
                        + [word] \
                        + [' ' for i in range(row_index + len(word), 15)])
  if len(word_as_col) > 15:
    raise InvalidTilePlacementError
  new_board = []
  for r in range(0, 15):
    if word_as_col[r] == ' ':
      new_board.append(board[r])
    elif board[r][col_index] == ' ':
      new_board.append(board[r][:col_index] \
                + word_as_col[r] \
                + board[r][col_index + 1:])
    else:
      raise InvalidTilePlacementError
  return tuple(new_board)
