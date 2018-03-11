from unittest import TestCase
from word_tree import make_word_tree
from scrabble.strategies import shape_first

class TestShape(TestCase):
  def test_first_move(self):
    board = ('               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ')
    self.assertEqual(('add_horizontal', ((7, 3), 'jumps')),
                     shape_first({'jumps'}, 
                                 make_word_tree(['jumps']),
                                 board, 
                                 'jumpszz'))

  def test_horizontal_intersection(self):
    board = ('               ',
             '               ',
             '               ',
             '       j       ',
             '       u       ',
             '       m       ',
             '       p       ',
             '       s       ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ')
    self.assertEqual(('add_horizontal', ((4, 6), 'crse')),
                     shape_first({'jumps','curse'}, 
                                 make_word_tree(['jumps', 'curse']),
                                 board, 
                                 'crsezzz'))

  def test_no_move(self):
    board = ('               ',
             '               ',
             '               ',
             '       j       ',
             '       u       ',
             '       m       ',
             '       p       ',
             '       s       ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ',
             '               ')
    self.assertEqual(('exchange_tiles', 'czsezzz'),
                     shape_first({'jumps','curse'}, 
                                 make_word_tree(['jumps', 'curse']),
                                 board, 
                                 'czsezzz'))
