from unittest import TestCase
from scrabble.board import new_board, add_horizontal

class TestBoard(TestCase):
  def test_new_board(self):
    b = new_board()
    for row in range(0, 15):
      for column in range(0, 15):
        self.assertEqual(' ', b[row][column])

  def test_add_hoizontal_valid(self):
    b = add_horizontal(new_board(), (5, 3), "remove")
    for row_index in (i for i in range(0, 15) if i != 5):
      self.assertEqual('               ', b[row_index])
    self.assertEqual('   remove      ', b[5])
