from unittest import TestCase
from scrabble.board import new_board
from scrabble.checker import get_words, is_valid_arrangement

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

class TestValidPlacement(TestCase):
  def test_empty_board(self):
    self.assertTrue(is_valid_arrangement(new_board()))

  def test_valid_single_word_horizontal(self):
    b = new_board()[:7] \
      + ('      xxxxxx    ',) \
      + new_board()[8:]
    self.assertTrue(is_valid_arrangement(b))

  def test_invalid_single_word_horizontal_wrong_row(self):
    b = new_board()[:6] \
      + ('      xxxxxx    ',) \
      + new_board()[7:]
    self.assertFalse(is_valid_arrangement(b))

  def test_invalid_single_word_horizontal_wrong_column(self):
    b = new_board()[:7] \
      + (' xxx            ',) \
      + new_board()[8:]
    self.assertFalse(is_valid_arrangement(b))

  def test_contiguous(self):
    b = new_board()[:5] \
      + ('        xxxx    ',
         '        x  x    ',
         '       xxx x    ',
         '      xxxxxx    ',
         '      xxxxxx    ') \
      + new_board()[10:]
    self.assertTrue(is_valid_arrangement(b))

  def test_disjoint(self):
    b = new_board()[:5] \
      + ('        xxxx    ',
         '                ',
         '       xxx x    ',
         '      xxxxxx    ',
         '      xxxxxx    ') \
      + new_board()[10:]
    self.assertFalse(is_valid_arrangement(b))

  #TODO: contiguous tiles check, edge and corner cases
