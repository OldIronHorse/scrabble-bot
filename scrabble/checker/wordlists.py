scowls = {}

def scowl(size):
  try:
    print('scowl({}) from cache'.format(size))
    return scowls[size]
  except KeyError:
    with open('scrabble/checker/scowl_{}.lst'.format(size), 
        'r', encoding='ISO-8859-1') as f:
      scowls[size] = {w.strip() for w in f.readlines()}
    return scowls[size]

