from itertools import permutations
from functools import reduce
from scrabble.board import new_board, add_horizontal, add_vertical
from scrabble.checker import is_valid_arrangement, get_words
from scrabble.scorer import score_move
from scrabble import InvalidTilePlacementError
#TODO: wordtree as alternative to brute force
#TODO: blank tile support

def basic(wordset, board0, tiles):
  if board0 == new_board():
    # first move
    candidate_words = {word for word 
                       in {''.join(w) for w 
                           in reduce(lambda acc, l: acc + list(l), 
                                     (permutations(tiles, n) for n 
                                      in range(2, len(tiles) + 1)), [])} 
                       if word in wordset}
    candidate_moves = [(word, board, score_move(board0, board)) 
                        for word, board in
                        [(word, add_horizontal(board0, 
                                               (7, 8 - len(word)), 
                                               word))
                         for word in candidate_words]]
    word, board, score  = \
      reduce(lambda best, move: move if move[2] > best[2] else best,
             candidate_moves)
    return ('add_horizontal', ((7, 8 - len(word)), word))
  # Not an empty board
  # whole words
  candidate_words = {word for word 
                     in {''.join(w) for w 
                         in reduce(lambda acc, l: acc + list(l), 
                                   (permutations(tiles, n) for n 
                                    in range(1, len(tiles) + 1)), [])}
                     if word in wordset}
  candidate_moves = []
  for r in range(0, 15):
    for c in range(0, 15):
      start = (r, c)
      for word in candidate_words:
        try:
          board_h = add_horizontal(board0, start, word)
          if is_valid_arrangement(board_h):
            candidate_moves.append((word, start, 'add_horizontal', board_h))
        except InvalidTilePlacementError:
          pass
        try:
          board_v = add_vertical(board0, start, word)
          if is_valid_arrangement(board_v):
            candidate_moves.append((word, start, 'add_vertical', board_v))
        except InvalidTilePlacementError:
          pass
  candidate_moves = [(word, start, action, board, score_move(board0, board)) 
                      for word, start, action, board 
                      in candidate_moves 
                      if get_words(board).issubset(wordset)]
  try:
    word, start, action, board, score = \
        reduce(lambda best, move: move if move[3] > best[3] else best, 
               candidate_moves)
    print(action, start, word, score)
    return (action, (start, word))
  except TypeError:
    print("no moves, returning tiles to bag")
    return('exchange_tiles', tiles)
