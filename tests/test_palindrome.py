import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(is_palindrome("No lemon no melon"))
    
    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("pepe honguito"))
        self.assertFalse(is_palindrome("computación"))
        self.assertFalse(is_palindrome("Ojalá apruebe computación"))
        self.assertFalse(is_palindrome("No es un palíndromo"))

    def edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("   "))
        self.assertTrue(is_palindrome("Anita lava la tina"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))
        self.assertTrue(is_palindrome("!@#$%^&*()_+"))
        self.assertTrue(is_palindrome("12321"))

if __name__ == '__main__':
    unittest.main()