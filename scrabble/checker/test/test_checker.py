from unittest import TestCase
from scrabble.board import new_board
from scrabble.checker import get_words

class TestGetWords(TestCase):
  def test_empty_board(self):
    self.assertEqual(set(), get_words(new_board()))

  def test_single_horizontal_word(self):
    b = new_board()[:6] \
      + ('    remove     ',) \
      + new_board()[7:]
    self.assertEqual({'remove'}, get_words(b))

  def test_multiple_horizontal_words(self):
    b = new_board()[:6] \
      + ('    remove     ',) \
      + new_board()[7:9] \
      + ('  dog          ',) \
      + new_board()[10:]
    self.assertEqual({'remove', 'dog'}, get_words(b))

  def test_multiple_horizontal_words_single_row(self):
    b = new_board()[:6] \
      + ('    remove dog ',) \
      + new_board()[7:]
    self.assertEqual({'remove','dog'}, get_words(b))

  def test_single_vertical_word(self):
    b = new_board()[:6] \
      + ('    r          ',
         '    e          ',
         '    m          ',
         '    o          ',
         '    v          ',
         '    e          ') \
      + new_board()[12:]
    self.assertEqual({'remove'}, get_words(b))

  def test_multiple_vertical_words(self):
    b = new_board()[:5] \
      + ('         d     ',
         '    r    o     ',
         '    e    g     ',
         '    m          ',
         '    o          ',
         '    v          ',
         '    e          ') \
      + new_board()[12:]
    self.assertEqual({'remove', 'dog'}, get_words(b))

  def test_multiple_vertical_words_single_column(self):
    b = new_board()[:2] \
      + ('    d          ',
         '    o          ',
         '    g          ',
         '               ',
         '    r          ',
         '    e          ',
         '    m          ',
         '    o          ',
         '    v          ',
         '    e          ') \
      + new_board()[12:]
    self.assertEqual({'remove', 'dog'}, get_words(b))

  def test_mixed_words(self):
    b = new_board()[:5] \
      + ('               ',
         '    r          ',
         '    e          ',
         '    m          ',
         '   dog         ',
         '    v          ',
         '    e          ') \
      + new_board()[12:]
    self.assertEqual({'remove', 'dog'}, get_words(b))

  def test_mixed_words_implied(self):
    b = new_board()[:5] \
      + ('               ',
         '    r          ',
         '    e          ',
         '    m          ',
         '   dog         ',
         '   ovoid       ',
         '    e          ') \
      + new_board()[12:]
    self.assertEqual({'remove', 'dog', 'do', 'go', 'ovoid'}, get_words(b))

  #TODO: mixed words, incl. implied 2-letter words
