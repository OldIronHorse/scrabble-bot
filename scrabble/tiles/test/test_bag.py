from unittest import TestCase
from scrabble.tiles import new_bag, shake

class TestBag(TestCase):
  def test_new_bag(self):
    bag = new_bag();
    self.assertEqual(9, len([tile for tile in bag if tile == 'a']))
    self.assertEqual(2, len([tile for tile in bag if tile == 'b']))
    self.assertEqual(2, len([tile for tile in bag if tile == 'c']))
    self.assertEqual(4, len([tile for tile in bag if tile == 'd']))
    self.assertEqual(12, len([tile for tile in bag if tile == 'e']))
    self.assertEqual(2, len([tile for tile in bag if tile == 'f']))
    self.assertEqual(3, len([tile for tile in bag if tile == 'g']))
    self.assertEqual(2, len([tile for tile in bag if tile == 'h']))
    self.assertEqual(9, len([tile for tile in bag if tile == 'i']))
    self.assertEqual(1, len([tile for tile in bag if tile == 'j']))
    self.assertEqual(1, len([tile for tile in bag if tile == 'k']))
    self.assertEqual(4, len([tile for tile in bag if tile == 'l']))
    self.assertEqual(2, len([tile for tile in bag if tile == 'm']))
    self.assertEqual(6, len([tile for tile in bag if tile == 'n']))
    self.assertEqual(8, len([tile for tile in bag if tile == 'o']))
    self.assertEqual(2, len([tile for tile in bag if tile == 'p']))
    self.assertEqual(1, len([tile for tile in bag if tile == 'q']))
    self.assertEqual(6, len([tile for tile in bag if tile == 'r']))
    self.assertEqual(4, len([tile for tile in bag if tile == 's']))
    self.assertEqual(6, len([tile for tile in bag if tile == 't']))
    self.assertEqual(4, len([tile for tile in bag if tile == 'u']))
    self.assertEqual(2, len([tile for tile in bag if tile == 'v']))
    self.assertEqual(2, len([tile for tile in bag if tile == 'w']))
    self.assertEqual(1, len([tile for tile in bag if tile == 'x']))
    self.assertEqual(2, len([tile for tile in bag if tile == 'y']))
    self.assertEqual(1, len([tile for tile in bag if tile == 'z']))
    self.assertEqual(2, len([tile for tile in bag if tile == '*']))

  def test_shake_bag(self):
    bag = new_bag()
    bag_s = shake(bag)
    self.assertNotEqual(bag, bag_s)
    self.assertEqual(sorted(bag), sorted(bag_s))
