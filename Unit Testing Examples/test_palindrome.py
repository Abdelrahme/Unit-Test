import unittest
import palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(palindrome.is_palindrome("racecar"))
        self.assertTrue(palindrome.is_palindrome("level"))
        self.assertFalse(palindrome.is_palindrome("hello"))
        self.assertFalse(palindrome.is_palindrome("world"))

if __name__ == '__main__':
    unittest.main()
