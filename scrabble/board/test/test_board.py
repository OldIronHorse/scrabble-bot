from unittest import TestCase
from scrabble.board import new_board, add_horizontal, add_vertical
from scrabble import InvalidTilePlacementError

class TestNewBoard(TestCase):
  def test_new_board(self):
    b = new_board()
    for row in range(0, 15):
      for column in range(0, 15):
        self.assertEqual(' ', b[row][column])


class TestAddHorizontal(TestCase):
  def test_add_hoizontal_valid_empty_board(self):
    starting_board = new_board()
    b = add_horizontal(starting_board, (5, 3), "remove")
    for row_index in (i for i in range(0, 15) if i != 5):
      self.assertEqual('               ', b[row_index])
    self.assertEqual('   remove      ', b[5])
    self.assertNotEqual(starting_board, b)
    
  def test_add_horizontal_valid_intersect(self):
    starting_board = new_board()
    starting_board = starting_board[:4] \
                    + ('      d        ',
                       '      o        ',
                       '      g        ') \
                    + starting_board[7:]
    b = add_horizontal(starting_board, (5, 3), "rem ve")
    for row_index in (i for i in range(0, 15) if i not in [4, 5,6]):
      self.assertEqual('               ', b[row_index])
    self.assertEqual('      d        ', b[4])
    self.assertEqual('   remove      ', b[5])
    self.assertEqual('      g        ', b[6])
    self.assertNotEqual(starting_board, b)

  def test_add_horizontal_invalid_intersect(self):
    starting_board = new_board()
    starting_board = starting_board[:4]\
                    + ('      d        ',
                       '      o        ',
                       '      g        ') \
                    + starting_board[7:]
    with self.assertRaises(InvalidTilePlacementError):
      add_horizontal(starting_board, (5, 3), "remove")

  def test_add_horizontal_invalid_off_board(self):
    starting_board = new_board()
    with self.assertRaises(InvalidTilePlacementError):
      add_horizontal(starting_board, (5, 12), "remove")


class TestAddVertical(TestCase):
  def test_add_vertical_valid_empty_board(self):
    starting_board = new_board()
    b = add_vertical(starting_board, (5, 3), "remove")
    self.assertEqual('   r           ', b[5])
    self.assertEqual('   e           ', b[6])
    self.assertEqual('   m           ', b[7])
    self.assertEqual('   o           ', b[8])
    self.assertEqual('   v           ', b[9])
    self.assertEqual('   e           ', b[10])
    for row_index in (i for i in range(0, 15) if i not in range(5, 11)):
      self.assertEqual('               ', b[row_index])
    self.assertNotEqual(starting_board, b)

  def test_add_vertical_valid_inertsect(self):
    starting_board = new_board()
    starting_board = starting_board[:5] \
                    + ('   remove      ',) \
                    + starting_board[6:]
    b = add_vertical(starting_board, (4, 6), "d g")
    for row_index in (i for i in range(0, 15) if i not in [4, 5,6]):
      self.assertEqual('               ', b[row_index])
    self.assertEqual('      d        ', b[4])
    self.assertEqual('   remove      ', b[5])
    self.assertEqual('      g        ', b[6])
    self.assertNotEqual(starting_board, b)

  def test_add_vertical_invalid_intersect(self):
    starting_board = new_board()
    starting_board = starting_board[:5] \
                    + ('   remove      ',) \
                    + starting_board[6:]
    with self.assertRaises(InvalidTilePlacementError):
      add_vertical(starting_board, (4, 6), "dog")

  def test_add_vertical_invalid_off_board(self):
    starting_board = new_board()
    with self.assertRaises(InvalidTilePlacementError):
      add_vertical(starting_board, (12, 5), "remove")
