from unittest import TestCase
from scrabble.scorer import score_word, score_move, get_words_and_squares
from scrabble.board import new_board, add_vertical, add_horizontal

class TestScoreWord(TestCase):
  def test_valid(self):
    self.assertEqual(0, score_word(''))
    self.assertEqual(6, score_word('mire'))
    self.assertEqual(6, score_word('the'))
    self.assertEqual(20, score_word('quick'))
    self.assertEqual(10, score_word('brown'))
    self.assertEqual(13, score_word('fox'))
    self.assertEqual(16, score_word('jumps'))
    self.assertEqual(7, score_word('over'))
    self.assertEqual(16, score_word('lazy'))
    self.assertEqual(5, score_word('dog'))


class TestGetWordsAndSquares(TestCase):
  def test_horizontal(self):
    b0 = add_horizontal(new_board(), (0,2), 'dog')
    self.assertEqual([('dog', ' d ')], get_words_and_squares(b0))

  def test_vertical(self):
    b0 = add_vertical(new_board(), (0,2), 'dog')
    self.assertEqual([('dog', '  D')], get_words_and_squares(b0))


#TODO: add special scoring squares
class TestScoreMove(TestCase):
  def test_no_special_squares(self):
    b0 = add_horizontal(new_board(), (4,0), 'dog')
    self.assertEqual(5, score_move(new_board(), b0))
    
  def test_double_letter(self):
    b0 = add_horizontal(new_board(), (0,2), 'dog')
    self.assertEqual(6, score_move(new_board(), b0))
    
  def test_moves(self):
    b0 = add_horizontal(new_board(), (7,3), 'jumps')
    # J on a double letter score, P on a double word score
    self.assertEqual(48, score_move(new_board(), b0))
    b1 = add_vertical(b0, (5,5), 'huan')
    # H & N on triple letter scores
    self.assertEqual(20, score_move(b0, b1))
    b2 = add_vertical(b1, (4,6), 'hopy')
    self.assertEqual(43, score_move(b1, b2))

