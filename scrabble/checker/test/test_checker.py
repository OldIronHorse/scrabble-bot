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


  #TODO: multiple words on multiple rows
  #TODO: multiple words on a single row
  #TODO: wrods in columns
