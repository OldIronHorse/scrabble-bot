from unittest import TestCase
from scrabble.scorer import score_word, score_move
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

#TODO: add special scoring squares
class TestScoreMove(TestCase):
  def test_moves(self):
    b0 = add_horizontal(new_board(), (7,3), 'jump')
    self.assertEqual(15, score_move(new_board(), b0))
    b1 = add_vertical(b0, (5,5), 'hu an')
    self.assertEqual(10, score_move(b0, b1))
    b2 = add_vertical(b1, (4,6), 'hop y')
    self.assertEqual(29, score_move(b1, b2))

