def scowl_35():
  global g_scowl_35
  if not g_scowl_35:
    with open('scrabble/checker/scowl_35.lst', 'r', encoding='ISO-8859-1') as f:
      g_scowl_35 = {w.strip() for w in f.readlines()}
  return g_scowl_35

g_scowl_35 = None
