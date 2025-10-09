#!/usr/bin/env python3
"""
Test suite for the Calculator program.
"""

import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0.1, 0.2), 0.30000000000000004)  # Float precision
        self.assertEqual(self.calc.add(-5, -3), -8)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(0.5, 4), 2.0)
    
    def test_division(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
        # Test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(4, 0.5), 2.0)
        self.assertEqual(self.calc.power(-2, 2), 4)
    
    def test_square_root(self):
        """Test square root operation."""
        self.assertEqual(self.calc.square_root(4), 2.0)
        self.assertEqual(self.calc.square_root(9), 3.0)
        self.assertEqual(self.calc.square_root(0), 0.0)
        self.assertAlmostEqual(self.calc.square_root(2), 1.4142135623730951)
        
        # Test square root of negative number
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_factorial(self):
        """Test factorial operation."""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)
        
        # Test factorial of negative number
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
        
        # Test factorial of large number
        with self.assertRaises(ValueError):
            self.calc.factorial(200)
    
    def test_trigonometric_functions(self):
        """Test trigonometric functions."""
        # Test sine
        self.assertAlmostEqual(self.calc.sin(0), 0, places=10)
        self.assertAlmostEqual(self.calc.sin(math.pi/2), 1, places=10)
        self.assertAlmostEqual(self.calc.sin(90, degrees=True), 1, places=10)
        
        # Test cosine
        self.assertAlmostEqual(self.calc.cos(0), 1, places=10)
        self.assertAlmostEqual(self.calc.cos(math.pi/2), 0, places=10)
        self.assertAlmostEqual(self.calc.cos(90, degrees=True), 0, places=10)
        
        # Test tangent
        self.assertAlmostEqual(self.calc.tan(0), 0, places=10)
        self.assertAlmostEqual(self.calc.tan(math.pi/4), 1, places=10)
        self.assertAlmostEqual(self.calc.tan(45, degrees=True), 1, places=10)
    
    def test_logarithm(self):
        """Test logarithm functions."""
        # Natural logarithm
        self.assertAlmostEqual(self.calc.log(math.e), 1, places=10)
        self.assertAlmostEqual(self.calc.log(1), 0, places=10)
        
        # Base 10 logarithm
        self.assertAlmostEqual(self.calc.log(10, 10), 1, places=10)
        self.assertAlmostEqual(self.calc.log(100, 10), 2, places=10)
        
        # Test logarithm of non-positive number
        with self.assertRaises(ValueError):
            self.calc.log(0)
        
        with self.assertRaises(ValueError):
            self.calc.log(-1)
        
        # Test invalid base
        with self.assertRaises(ValueError):
            self.calc.log(10, 0)
        
        with self.assertRaises(ValueError):
            self.calc.log(10, 1)
    
    def test_memory_operations(self):
        """Test memory operations."""
        # Test initial memory
        self.assertEqual(self.calc.memory_recall(), 0)
        
        # Test memory store and recall
        self.calc.memory_store(42)
        self.assertEqual(self.calc.memory_recall(), 42)
        
        # Test memory clear
        self.calc.memory_clear()
        self.assertEqual(self.calc.memory_recall(), 0)
    
    def test_history(self):
        """Test calculation history."""
        # Test initial history
        self.assertEqual(len(self.calc.get_history()), 0)
        
        # Perform some operations
        self.calc.add(2, 3)
        self.calc.multiply(4, 5)
        self.calc.subtract(10, 3)
        
        # Check history
        history = self.calc.get_history()
        self.assertEqual(len(history), 3)
        self.assertIn("2 + 3 = 5", history[0])
        self.assertIn("4 × 5 = 20", history[1])
        self.assertIn("10 - 3 = 7", history[2])
        
        # Test clear history
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)
    
    def test_history_limit(self):
        """Test that history is limited to 100 operations."""
        # Add more than 100 operations
        for i in range(105):
            self.calc.add(i, 1)
        
        # Check that history is limited to 100
        history = self.calc.get_history()
        self.assertEqual(len(history), 100)
        
        # Check that oldest operations were removed
        self.assertNotIn("0 + 1 = 1", history)
        self.assertIn("104 + 1 = 105", history)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_large_numbers(self):
        """Test operations with large numbers."""
        large_num = 1e10
        self.assertEqual(self.calc.add(large_num, large_num), 2e10)
        self.assertEqual(self.calc.multiply(large_num, 2), 2e10)
    
    def test_small_numbers(self):
        """Test operations with very small numbers."""
        small_num = 1e-10
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 2e-10)
        self.assertAlmostEqual(self.calc.multiply(small_num, 2), 2e-10)
    
    def test_precision(self):
        """Test floating point precision issues."""
        # This is a known floating point precision issue
        result = self.calc.add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=10)
    
    def test_infinity_and_nan(self):
        """Test handling of infinity and NaN."""
        # Test with infinity
        inf = float('inf')
        self.assertEqual(self.calc.add(inf, 1), inf)
        self.assertTrue(math.isnan(self.calc.subtract(inf, inf)))
        
        # Test with NaN
        nan = float('nan')
        self.assertTrue(math.isnan(self.calc.add(nan, 1)))


def run_tests():
    """Run all tests and display results."""
    print("🧪 Running Calculator Tests...")
    print("=" * 50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorEdgeCases))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print(f"❌ {len(result.failures)} test(s) failed")
        print(f"❌ {len(result.errors)} error(s) occurred")
    
    print(f"📊 Tests run: {result.testsRun}")
    print("=" * 50)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
