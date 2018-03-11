import time
from itertools import repeat, permutations
from functools import reduce
from word_tree import next_char
from scrabble.scorer import score_move
from scrabble.checker import is_valid_arrangement, get_words
from scrabble.board import add_horizontal
from scrabble import InvalidTilePlacementError

all_starts = sum([[(r, c) for c in range(0, 15)] for r in range(0, 15)], [])
all_shapes = [''.join(repeat('-', n)) for n in range(1, 8)]

def add_horizontal_silent(board, start, word):
  try:
    return add_horizontal(board, start, word)
  except InvalidTilePlacementError:
    #print('failing silently:', start, word)
    return board

def find_words(wordtree, fixed_letters, letters, 
               laid_so_far='', 
               word_so_far=''):
  #print('|{}|'.format(fixed_letters), letters, word_so_far)
  next_chars = next_char(wordtree, word_so_far)
  #print('next_chars:', next_chars)

  if not fixed_letters:
    if None in next_chars:
      return [laid_so_far]
    else:
      return []
  elif fixed_letters[0] == ' ':
    return sum([find_words(wordtree, fixed_letters[1:], 
                           letters.replace(c,'',1), 
                           laid_so_far + c,
                           word_so_far + c)
                for c in next_chars if c and c in letters], [])
  elif fixed_letters[0] in next_chars:
    return find_words(wordtree, fixed_letters[1:],
                      letters, laid_so_far, word_so_far + fixed_letters[0])
  else:
    return []

def shape_first(wordset, wordtree, board0, tiles):
  #begin = time.time()
  shapes = all_shapes[:len(tiles)]
  h_moves = [(start, length)
             for board1, start, length
             in [(add_horizontal_silent(board0, start, shape), start, 
                  len(shape)) 
                 for start, shape 
                 in sum([[((r,c), shape) 
                          for shape 
                          in all_shapes 
                          if (c + len(shape) < 16)] 
                         for (r,c) 
                         in all_starts], [])]
             if is_valid_arrangement(board1)]
  #print('h_moves:', h_moves)
  #print(time.time() - begin,'sec')
  #begin = time.time()
  #print('#h_moves:', len(h_moves))
  h_moves_word = []
  for (r, c), length in h_moves:
    for word in find_words(wordtree, board0[r][c:c + length], tiles):
      h_moves_word.append((add_horizontal(board0, (r,c), word),
                          (r, c), word, 'add_horizontal'))
  #print(time.time() - begin,'sec')
  #begin = time.time()
  #print('#h_moves_word:', len(h_moves_word))
  moves_scored = [((action, (start, word)), score_move(board0, board1))
                  for board1, start, word, action
                  in h_moves_word
                  if get_words(board1).issubset(wordset)
                    and board1 != board0]
  try:
    best_move, score = reduce(lambda acc, m: m if m[1] > acc[1] else acc,
                              moves_scored)
    #print(time.time() - begin,'sec')
    #print(best_move, score)
    return best_move
  except TypeError:
    pass
  #print(time.time() - begin,'sec')
  return ('exchange_tiles', tiles)

