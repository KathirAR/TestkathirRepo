#!/usr/bin/env python3
"""
Unit tests for the palindrome module.

Author: Kathir (via Codegen)
"""

import unittest
from palindrome import (
    is_palindrome_simple,
    is_palindrome,
    is_number_palindrome,
    find_palindromes,
    longest_palindrome
)


class TestPalindromeSimple(unittest.TestCase):
    """Test cases for is_palindrome_simple function."""
    
    def test_simple_palindromes(self):
        """Test basic palindrome cases."""
        self.assertTrue(is_palindrome_simple("racecar"))
        self.assertTrue(is_palindrome_simple("level"))
        self.assertTrue(is_palindrome_simple(""))
        self.assertTrue(is_palindrome_simple("a"))
        
    def test_simple_non_palindromes(self):
        """Test basic non-palindrome cases."""
        self.assertFalse(is_palindrome_simple("hello"))
        self.assertFalse(is_palindrome_simple("world"))
        self.assertFalse(is_palindrome_simple("python"))
        
    def test_case_sensitive(self):
        """Test that simple function is case-sensitive."""
        self.assertFalse(is_palindrome_simple("Racecar"))
        self.assertFalse(is_palindrome_simple("Level"))
        
    def test_with_spaces_and_punctuation(self):
        """Test that simple function includes spaces and punctuation."""
        self.assertFalse(is_palindrome_simple("race car"))
        self.assertFalse(is_palindrome_simple("A man a plan a canal Panama"))
        
    def test_invalid_input(self):
        """Test error handling for invalid input."""
        with self.assertRaises(TypeError):
            is_palindrome_simple(123)
        with self.assertRaises(TypeError):
            is_palindrome_simple(None)


class TestPalindrome(unittest.TestCase):
    """Test cases for is_palindrome function."""
    
    def test_basic_palindromes(self):
        """Test basic palindrome cases."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        
    def test_case_insensitive(self):
        """Test case-insensitive palindromes."""
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("Level"))
        self.assertTrue(is_palindrome("Madam"))
        
    def test_with_spaces(self):
        """Test palindromes with spaces."""
        self.assertTrue(is_palindrome("race car"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("never odd or even"))
        
    def test_with_punctuation(self):
        """Test palindromes with punctuation."""
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("Madam, I'm Adam"))
        self.assertTrue(is_palindrome("A Santa at NASA"))
        
    def test_non_palindromes(self):
        """Test non-palindrome cases."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertFalse(is_palindrome("not a palindrome"))
        
    def test_options(self):
        """Test different option combinations."""
        # Case sensitive
        self.assertFalse(is_palindrome("Racecar", ignore_case=False))
        self.assertTrue(is_palindrome("racecar", ignore_case=False))
        
        # Include spaces
        self.assertFalse(is_palindrome("race car", ignore_spaces=False))
        self.assertTrue(is_palindrome("racecar", ignore_spaces=False))
        
        # Include punctuation
        self.assertFalse(is_palindrome("race,car", ignore_punctuation=False))
        self.assertTrue(is_palindrome("racecar", ignore_punctuation=False))
        
    def test_invalid_input(self):
        """Test error handling for invalid input."""
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome(None)


class TestNumberPalindrome(unittest.TestCase):
    """Test cases for is_number_palindrome function."""
    
    def test_integer_palindromes(self):
        """Test integer palindromes."""
        self.assertTrue(is_number_palindrome(121))
        self.assertTrue(is_number_palindrome(1221))
        self.assertTrue(is_number_palindrome(7))
        self.assertTrue(is_number_palindrome(0))
        
    def test_integer_non_palindromes(self):
        """Test integer non-palindromes."""
        self.assertFalse(is_number_palindrome(123))
        self.assertFalse(is_number_palindrome(1234))
        self.assertFalse(is_number_palindrome(10))
        
    def test_float_palindromes(self):
        """Test float palindromes."""
        self.assertTrue(is_number_palindrome(12.21))
        self.assertTrue(is_number_palindrome(1.1))
        self.assertTrue(is_number_palindrome(123.321))
        
    def test_float_non_palindromes(self):
        """Test float non-palindromes."""
        self.assertFalse(is_number_palindrome(12.34))
        self.assertFalse(is_number_palindrome(1.23))
        self.assertFalse(is_number_palindrome(123.45))
        
    def test_whole_number_floats(self):
        """Test floats that are whole numbers."""
        self.assertTrue(is_number_palindrome(121.0))
        self.assertFalse(is_number_palindrome(123.0))
        
    def test_negative_numbers(self):
        """Test negative numbers."""
        self.assertFalse(is_number_palindrome(-121))  # "-121" != "121-"
        self.assertFalse(is_number_palindrome(-12.21))
        
    def test_invalid_input(self):
        """Test error handling for invalid input."""
        with self.assertRaises(TypeError):
            is_number_palindrome("123")
        with self.assertRaises(TypeError):
            is_number_palindrome(None)


class TestFindPalindromes(unittest.TestCase):
    """Test cases for find_palindromes function."""
    
    def test_find_basic_palindromes(self):
        """Test finding basic palindromes."""
        result = find_palindromes("abccba")
        self.assertIn("abccba", result)
        self.assertIn("bccb", result)
        
    def test_find_with_min_length(self):
        """Test finding palindromes with minimum length."""
        result = find_palindromes("abccba", min_length=4)
        self.assertIn("abccba", result)
        self.assertIn("bccb", result)
        self.assertNotIn("cc", result)
        
    def test_find_overlapping_palindromes(self):
        """Test finding overlapping palindromes."""
        result = find_palindromes("aabaa")
        self.assertIn("aabaa", result)
        self.assertIn("aba", result)
        
    def test_no_palindromes_found(self):
        """Test when no palindromes are found."""
        result = find_palindromes("abcdef")
        self.assertEqual(result, [])
        
    def test_case_preservation(self):
        """Test that original case is preserved."""
        result = find_palindromes("AbCcBa")
        self.assertIn("AbCcBa", result)
        
    def test_invalid_input(self):
        """Test error handling for invalid input."""
        with self.assertRaises(TypeError):
            find_palindromes(123)
        with self.assertRaises(ValueError):
            find_palindromes("test", min_length=0)


class TestLongestPalindrome(unittest.TestCase):
    """Test cases for longest_palindrome function."""
    
    def test_longest_basic(self):
        """Test finding longest palindrome in basic cases."""
        self.assertEqual(longest_palindrome("babad"), "bab")
        self.assertEqual(longest_palindrome("cbbd"), "bb")
        
    def test_longest_single_character(self):
        """Test with single character."""
        self.assertEqual(longest_palindrome("a"), "a")
        
    def test_longest_empty_string(self):
        """Test with empty string."""
        self.assertEqual(longest_palindrome(""), "")
        
    def test_longest_no_palindrome(self):
        """Test when no multi-character palindrome exists."""
        result = longest_palindrome("abcdef")
        self.assertEqual(len(result), 1)  # Should return single character
        
    def test_longest_entire_string(self):
        """Test when entire string is a palindrome."""
        self.assertEqual(longest_palindrome("racecar"), "racecar")
        
    def test_longest_case_insensitive(self):
        """Test case-insensitive longest palindrome."""
        result = longest_palindrome("AbCcBa")
        self.assertEqual(result.lower(), result.lower()[::-1])
        
    def test_invalid_input(self):
        """Test error handling for invalid input."""
        with self.assertRaises(TypeError):
            longest_palindrome(123)


class TestIntegration(unittest.TestCase):
    """Integration tests combining multiple functions."""
    
    def test_comprehensive_palindrome_analysis(self):
        """Test comprehensive analysis of a text."""
        text = "A man a plan a canal Panama racecar"
        
        # Check if entire text is palindrome
        is_full_palindrome = is_palindrome(text)
        
        # Find all palindromes
        all_palindromes = find_palindromes(text, min_length=3)
        
        # Find longest palindrome
        longest = longest_palindrome(text)
        
        # Verify results make sense
        self.assertIsInstance(is_full_palindrome, bool)
        self.assertIsInstance(all_palindromes, list)
        self.assertIsInstance(longest, str)
        self.assertGreaterEqual(len(longest), 1)


if __name__ == "__main__":
    # Run all tests
    unittest.main(verbosity=2)
