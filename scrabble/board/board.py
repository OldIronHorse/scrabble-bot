from scrabble import InvalidTilePlacementError

def new_board():
  return ['               ' for i in range (0, 15)]

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
  return board[:row_index] + [new_row] + board[row_index + 1:]
