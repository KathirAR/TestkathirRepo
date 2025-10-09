#!/usr/bin/env python3
"""
Unit tests for palindrome.py

Author: Kathir (via Codegen)
"""

import unittest
from palindrome import (
    is_palindrome,
    is_numeric_palindrome,
    longest_palindromic_substring,
    generate_palindromes,
    find_palindromes_in_text
)


class TestPalindrome(unittest.TestCase):
    """Test cases for palindrome functions."""
    
    def test_is_palindrome_basic(self):
        """Test basic palindrome checking."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
    
    def test_is_palindrome_case_insensitive(self):
        """Test case-insensitive palindrome checking."""
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("MadAm"))
        self.assertTrue(is_palindrome("A"))
        self.assertFalse(is_palindrome("Hello"))
    
    def test_is_palindrome_with_spaces(self):
        """Test palindrome checking with spaces and punctuation."""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("race car", ignore_spaces=False))    # False with spaces
        self.assertTrue(is_palindrome("taco cat", ignore_spaces=True))      # True when ignoring spaces
        self.assertFalse(is_palindrome("taco cat", ignore_spaces=False))    # False with spaces
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
    
    def test_is_numeric_palindrome(self):
        """Test numeric palindrome checking."""
        self.assertTrue(is_numeric_palindrome(121))
        self.assertTrue(is_numeric_palindrome(12321))
        self.assertTrue(is_numeric_palindrome(1))
        self.assertTrue(is_numeric_palindrome(1001))
        self.assertFalse(is_numeric_palindrome(123))
        self.assertFalse(is_numeric_palindrome(12345))
    
    def test_longest_palindromic_substring(self):
        """Test finding longest palindromic substring."""
        self.assertEqual(longest_palindromic_substring("babad"), "bab")
        self.assertEqual(longest_palindromic_substring("cbbd"), "bb")
        self.assertEqual(longest_palindromic_substring(""), "")
        self.assertEqual(longest_palindromic_substring("a"), "a")
        self.assertEqual(longest_palindromic_substring("racecar"), "racecar")
    
    def test_generate_palindromes_length_1(self):
        """Test generating palindromes of length 1."""
        palindromes = generate_palindromes(1)
        self.assertEqual(len(palindromes), 26)  # 26 letters
        self.assertIn("a", palindromes)
        self.assertIn("z", palindromes)
    
    def test_generate_palindromes_length_2(self):
        """Test generating palindromes of length 2."""
        palindromes = generate_palindromes(2)
        self.assertEqual(len(palindromes), 26)  # aa, bb, cc, ..., zz
        self.assertIn("aa", palindromes)
        self.assertIn("zz", palindromes)
        # All should be of length 2
        for p in palindromes:
            self.assertEqual(len(p), 2)
            self.assertEqual(p[0], p[1])
    
    def test_generate_palindromes_invalid_length(self):
        """Test generating palindromes with invalid length."""
        self.assertEqual(generate_palindromes(0), [])
        self.assertEqual(generate_palindromes(-1), [])
    
    def test_find_palindromes_in_text(self):
        """Test finding palindromes in text."""
        text = "The racecar was fast, madam!"
        palindromes = find_palindromes_in_text(text)
        self.assertIn("racecar", palindromes)
        self.assertIn("madam", palindromes)
        
        # Test with minimum length
        palindromes_min_5 = find_palindromes_in_text(text, min_length=5)
        self.assertIn("racecar", palindromes_min_5)
        self.assertIn("madam", palindromes_min_5)
    
    def test_find_palindromes_empty_text(self):
        """Test finding palindromes in empty text."""
        palindromes = find_palindromes_in_text("")
        self.assertEqual(palindromes, [])


def run_tests():
    """Run all tests and display results."""
    print("🧪 Running Palindrome Tests...")
    print("=" * 30)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPalindrome)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 30)
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print(f"❌ {len(result.failures)} test(s) failed")
        print(f"❌ {len(result.errors)} error(s) occurred")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
