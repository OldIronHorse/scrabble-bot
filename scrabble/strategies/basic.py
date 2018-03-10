from itertools import permutations
from functools import reduce
from scrabble.board import new_board, add_horizontal, add_vertical
from scrabble.checker import is_valid_arrangement, get_words
from scrabble.scorer import score_move
from scrabble import InvalidTilePlacementError
#TODO: wordtree as alternative to brute force
#TODO: blank tile support

def shortest_first(wordset, board0, tiles):
  for n in range(1, len(tiles)):
    print('n:', n)
    candidate_words = {''.join(w) for w in permutations(tiles, n)}
    print('candidate_words:', len(candidate_words))
    candidate_moves = all_legal_moves(wordset, board0, candidate_words)
    print('candidate_moves', len(candidate_moves))
    try:
      return highest_scoring(candidate_moves)
    except TypeError:
      pass
  print("no moves, returning tiles to bag")
  return('exchange_tiles', tiles)

def longest_first(wordset, board0, tiles):
  for n in range(len(tiles), 1, -1):
    print('n:', n)
    candidate_words = {''.join(w) for w in permutations(tiles, n)}
    print('candidate_words:', len(candidate_words))
    candidate_moves = all_legal_moves(wordset, board0, candidate_words)
    print('candidate_moves', len(candidate_moves))
    try:
      return highest_scoring(candidate_moves)
    except TypeError:
      pass
  print("no moves, returning tiles to bag")
  return('exchange_tiles', tiles)

def whole_words(wordset, board0, tiles):
  # whole words
  candidate_words = {word for word 
                     in {''.join(w) for w 
                         in reduce(lambda acc, l: acc + list(l), 
                                   (permutations(tiles, n) for n 
                                    in range(1, len(tiles) + 1)), [])}
                     if word in wordset}
  print('candidate_words:', len(candidate_words))
  candidate_moves = all_legal_moves(wordset, board0, candidate_words)
  print('candidate_moves', len(candidate_moves))
  try:
    return highest_scoring(candidate_moves)
  except TypeError:
    print("no moves, returning tiles to bag")
    return('exchange_tiles', tiles)

def all_legal_moves(wordset, board0, candidate_words):
  candidate_moves = []
  for r in range(0, 15):
    for c in range(0, 15):
      if board0[r][c] == ' ':
        start = (r, c)
        for word in candidate_words:
          if c + len(word) < 15:
            try:
              board_h = add_horizontal(board0, start, word)
              if is_valid_arrangement(board_h):
                candidate_moves.append((word, start, 'add_horizontal', board_h))
            except InvalidTilePlacementError:
              pass
          if r + len(word) < 15:
            try:
              board_v = add_vertical(board0, start, word)
              if is_valid_arrangement(board_v):
                candidate_moves.append((word, start, 'add_vertical', board_v))
            except InvalidTilePlacementError:
              pass
  print(' moves before spellcheck', len(candidate_moves))
  return [(word, start, action, board, score_move(board0, board)) 
          for word, start, action, board 
          in candidate_moves 
          if get_words(board).issubset(wordset)]

def highest_scoring(candidate_moves):
  word, start, action, board, score = \
      reduce(lambda best, move: move if move[3] > best[3] else best, 
             candidate_moves)
  print(action, start, word, score)
  return (action, (start, word))
