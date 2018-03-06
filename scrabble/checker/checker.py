def get_words(board):
  words = {w for w in {r.strip() for r in board} if len(w) > 1}
  return words
