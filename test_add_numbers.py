#!/usr/bin/env python3
"""
Test module for add_numbers.py
"""

import unittest
from add_numbers import add_two_numbers


class TestAddNumbers(unittest.TestCase):
    """Test cases for the add_two_numbers function."""
    
    def test_add_positive_integers(self):
        """Test adding positive integers."""
        self.assertEqual(add_two_numbers(5, 3), 8)
        self.assertEqual(add_two_numbers(10, 20), 30)
    
    def test_add_negative_integers(self):
        """Test adding negative integers."""
        self.assertEqual(add_two_numbers(-5, -3), -8)
        self.assertEqual(add_two_numbers(-10, 5), -5)
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        self.assertAlmostEqual(add_two_numbers(2.5, 1.5), 4.0)
        self.assertAlmostEqual(add_two_numbers(3.14, 2.86), 6.0)
    
    def test_add_zero(self):
        """Test adding with zero."""
        self.assertEqual(add_two_numbers(0, 5), 5)
        self.assertEqual(add_two_numbers(10, 0), 10)
        self.assertEqual(add_two_numbers(0, 0), 0)
    
    def test_add_mixed_types(self):
        """Test adding integer and float."""
        self.assertEqual(add_two_numbers(5, 2.5), 7.5)
        self.assertEqual(add_two_numbers(3.5, 2), 5.5)


if __name__ == "__main__":
    unittest.main()

