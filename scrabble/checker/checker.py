from functools import reduce

def words(lines):
  return {w for w 
            in reduce(lambda r1, r2: r1 + r2, 
                      [r.split(' ') for r in lines]) 
            if len(w) > 1}

def get_words(board):
  cols = []
  for col in range(0, 15):
    column = []
    for row in range(0, 15):
      column.append(board[row][col])
    cols.append(''.join(column))
  return words(board) | words(cols)
