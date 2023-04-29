import unittest
import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle1 = Rectangle.Rectangle(3, 4)
        self.rectangle2 = Rectangle.Rectangle(5, 5)

    def test_area(self):
        self.assertEqual(self.rectangle1.area(), 12)
        self.assertEqual(self.rectangle2.area(), 25)

    def test_perimeter(self):
        self.assertEqual(self.rectangle1.perimeter(), 14)
        self.assertEqual(self.rectangle2.perimeter(), 20)

    def test_is_square(self):
        self.assertFalse(self.rectangle1.is_square())
        self.assertTrue(self.rectangle2.is_square())

if __name__ == '__main__':
    unittest.main()
