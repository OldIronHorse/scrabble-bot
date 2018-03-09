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

multipliers = {
  't': lambda n: 3 * n,
  'd': lambda n: 2 * n,
  'D': lambda n: n,
  'T': lambda n: n,
  ' ': lambda n: n,
}

def score_move(board0, board1):
  score = 0
  for row in [tuple(zip(row0, row1, row_s)) for row0, row1, row_s in zip(board0, board1, squares)]:
    for t0, t1, s in row:
      score += multipliers[s](points[t1])
  return score
  #(t0,t1,s,p)
  #for row in map(lambda row: map(lambda square: square + (multiplers[square[2]](points[square[1]]),), row), 
                 #map(lambda row: zip(row[0], row[1], row[2]), 
                     #zip(board0, board1, squares))):
    #print()
    #for square in row:
      #print(square)

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
