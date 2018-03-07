from itertools import permutations
from functools import reduce
from scrabble.board import new_board, add_horizontal, add_vertical
from scrabble.checker import scowl_35, is_valid_arrangement, get_words
from scrabble.scorer import score_move
from scrabble import InvalidTilePlacementError
#TODO: wordtree as alternative to brute force
#TODO: blank tile support

def basic(game, player):
  print(player)
  if game['board'] == new_board():
    # first move
    candidate_words = {word for word in {''.join(w) for w in reduce(lambda acc, l: acc + list(l), (permutations(player['tiles'], n) for n in range(2, len(player['tiles']) + 1)), [])} if word in scowl_35()}
    print(candidate_words)
    candidate_moves = [(word, board, score_move(game['board'], board)) 
                        for word, board in
                        [(word, add_horizontal(game['board'], 
                                               (7, 8 - len(word)), 
                                               word))
                         for word in candidate_words]]
    word, board, score  = \
      reduce(lambda best, move: move if move[2] > best[2] else best,
             candidate_moves)
    print(word, score)
    #TODO: should the strategy function be updating the game and player state directly?
    game['board'] = board
    tiles = list(player['tiles'])
    for l in word:
      tiles.remove(l)
    player['tiles'] = ''.join(tiles)
    player['score'] += score
  else:
    # whole words
    candidate_words = {word for word in {''.join(w) for w in reduce(lambda acc, l: acc + list(l), (permutations(player['tiles'], n) for n in range(1, len(player['tiles']) + 1)), [])} if word in scowl_35()}
    candidate_moves = []
    for r in range(0, 15):
      for c in range(0, 15):
        start = (r, c)
        for word in candidate_words:
          try:
            board_h = add_horizontal(game['board'], start, word)
            if is_valid_arrangement(board_h):
              candidate_moves.append((word, start, board_h))
          except InvalidTilePlacementError:
            pass
          try:
            board_v = add_vertical(game['board'], start, word)
            if is_valid_arrangement(board_v):
              candidate_moves.append((word, start, board_v))
          except InvalidTilePlacementError:
            pass
    candidate_moves = [(word, start, board, score_move(game['board'], board)) for word, start, board \
                        in candidate_moves if get_words(board).issubset(scowl_35())]
    word, start, board, score = reduce(lambda best, move: move if move[3] > best[3] else best, candidate_moves)
    game['board'] = board
    tiles = list(player['tiles'])
    for l in word:
      tiles.remove(l)
    player['tiles'] = ''.join(tiles)
    player['score'] += score

