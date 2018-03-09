from scrabble.checker import get_words

points = {
  'a': 1,
  'b': 3,
  'c': 3,
  'd': 2,
  'e': 1,
  'f': 4,
  'g': 2,
  'h': 4,
  'i': 1,
  'j': 8,
  'k': 5,
  'l': 1,
  'm': 3,
  'n': 1,
  'o': 1,
  'p': 3,
  'q': 10,
  'r': 1,
  's': 1,
  't': 1,
  'u': 1,
  'v': 4,
  'w': 4,
  'x': 8,
  'y': 4,
  'z': 10,
  ' ': 0,
}

def score_word(word):
  return sum([points[l] for l in word])

letter_multipliers = {
  't': 3,
  'd': 2,
  'D': 1,
  'T': 1,
  ' ': 1,
}

word_multipliers = {
  't': 1,
  'd': 1,
  'D': 2,
  'T': 3,
  ' ': 1,
}

squares = ('T  d   T   d  T',
           ' D   t   t   D ',
           '  D   d d   D  ',
           'd  D   d   D  d',
           '    D     D    ',
           ' t   t   t   t ',
           '  d   d d   d  ',
           'T  d   D   d  T',
           '  d   d d   d  ',
           ' t   t   t   t ',
           '    D     D    ',
           'd  D   d   D  d',
           '  D   d d   D  ',
           ' D   t   t   D ',
           'T  d   T   d  T')

def get_words_and_squares(board, available_squares=squares):
  return get_words_and_squares_from_rows(board, available_squares) \
      + get_words_and_squares_from_rows(list(map(lambda row: ''.join(row), 
                                                 zip(*board))), 
                                        available_squares)

def get_words_and_squares_from_rows(board, available_squares):
  words_squares = []
  for r in range(0, len(board)):
    start_index = None
    for c in range(0, len(board[r])):
      if board[r][c] == ' ':
        if start_index is not None:
          if c - start_index > 1:
            words_squares.append((board[r][start_index:c], 
                                  available_squares[r][start_index:c]))
        start_index = None
      elif start_index is None:
        start_index = c
  return words_squares

def score_move(board0, board1):
  #[('dog', ' d '),....]
  #TODO: exclude squares that weren't covered in this move
  available_squares = [[s if t == ' ' else ' ' for t, s in row] for row
                       in (zip(rb, rs) for rb, rs
                           in zip(board0, squares))]
  words_squares0 = get_words_and_squares(board0, available_squares)
  words_squares1 = get_words_and_squares(board1, available_squares)
  for ws in words_squares0:
    words_squares1.remove(ws)
  score = 0
  print(words_squares1)
  for word, sqs in words_squares1:
    word_score = 0
    word_multiplier = 1
    for l, s in zip(word, sqs):
      word_multiplier *= word_multipliers[s]
      word_score += (points[l] * letter_multipliers[s])
      print(l,s,word_score, word_multiplier)
    word_score *= word_multiplier
    score += word_score
  return score
