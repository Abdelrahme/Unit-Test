import unittest
import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        lst = [1, 3, 5, 7, 9, 11]
        self.assertEqual(binary_search.binary_search(lst, 1), 0)
        self.assertEqual(binary_search.binary_search(lst, 3), 1)
        self.assertEqual(binary_search.binary_search(lst, 5), 2)
        self.assertEqual(binary_search.binary_search(lst, 7), 3)
        self.assertEqual(binary_search.binary_search(lst, 9), 4)
        self.assertEqual(binary_search.binary_search(lst, 11), 5)
        self.assertEqual(binary_search.binary_search(lst, 0), -1)
        self.assertEqual(binary_search.binary_search(lst, 2), -1)
        self.assertEqual(binary_search.binary_search(lst, 6), -1)
        self.assertEqual(binary_search.binary_search(lst, 10), -1)
        self.assertEqual(binary_search.binary_search(lst, 12), -1)

if __name__ == '__main__':
    unittest.main()
