#!/usr/bin/env python3
"""
Test suite for the Calculator Program
Tests all calculator functions to ensure they work correctly.
Author: Codegen (for ClickUp task #86d0jt9dz)
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
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)
    
    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(10, 15), -5)
    
    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
    
    def test_division(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        
        # Test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
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
        
        # Test negative number
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_factorial(self):
        """Test factorial operation."""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)
        
        # Test negative number
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
    
    def test_trigonometric_functions(self):
        """Test trigonometric functions."""
        # Test with radians
        self.assertAlmostEqual(self.calc.sin(0), 0, places=10)
        self.assertAlmostEqual(self.calc.sin(math.pi/2), 1, places=10)
        self.assertAlmostEqual(self.calc.cos(0), 1, places=10)
        self.assertAlmostEqual(self.calc.cos(math.pi), -1, places=10)
        self.assertAlmostEqual(self.calc.tan(0), 0, places=10)
        
        # Test with degrees
        self.assertAlmostEqual(self.calc.sin(90, degrees=True), 1, places=10)
        self.assertAlmostEqual(self.calc.cos(180, degrees=True), -1, places=10)
        self.assertAlmostEqual(self.calc.tan(45, degrees=True), 1, places=10)
    
    def test_logarithm(self):
        """Test logarithm operation."""
        # Natural logarithm
        self.assertAlmostEqual(self.calc.log(math.e), 1, places=10)
        self.assertAlmostEqual(self.calc.log(1), 0, places=10)
        
        # Base 10 logarithm
        self.assertAlmostEqual(self.calc.log(100, 10), 2, places=10)
        self.assertAlmostEqual(self.calc.log(1000, 10), 3, places=10)
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            self.calc.log(0)
        with self.assertRaises(ValueError):
            self.calc.log(-1)
        with self.assertRaises(ValueError):
            self.calc.log(10, 0)
        with self.assertRaises(ValueError):
            self.calc.log(10, 1)
    
    def test_percentage(self):
        """Test percentage calculation."""
        self.assertEqual(self.calc.percentage(100, 50), 50)
        self.assertEqual(self.calc.percentage(200, 25), 50)
        self.assertEqual(self.calc.percentage(80, 125), 100)
        self.assertEqual(self.calc.percentage(0, 50), 0)
    
    def test_expression_evaluator(self):
        """Test expression evaluation."""
        self.assertEqual(self.calc.evaluate_expression("2 + 3"), 5)
        self.assertEqual(self.calc.evaluate_expression("10 - 4"), 6)
        self.assertEqual(self.calc.evaluate_expression("3 * 4"), 12)
        self.assertEqual(self.calc.evaluate_expression("15 / 3"), 5)
        self.assertEqual(self.calc.evaluate_expression("2 ** 3"), 8)
        self.assertAlmostEqual(self.calc.evaluate_expression("sqrt(16)"), 4, places=10)
        self.assertAlmostEqual(self.calc.evaluate_expression("sin(0)"), 0, places=10)
        
        # Test complex expressions
        self.assertEqual(self.calc.evaluate_expression("(2 + 3) * 4"), 20)
        self.assertAlmostEqual(self.calc.evaluate_expression("pi"), math.pi, places=10)
        self.assertAlmostEqual(self.calc.evaluate_expression("e"), math.e, places=10)
        
        # Test invalid expressions
        with self.assertRaises(ValueError):
            self.calc.evaluate_expression("2 + ")
        with self.assertRaises(ValueError):
            self.calc.evaluate_expression("invalid_function(5)")
    
    def test_history_tracking(self):
        """Test calculation history functionality."""
        # Initially empty
        self.assertEqual(len(self.calc.get_history()), 0)
        
        # Add some calculations
        self.calc.add(2, 3)
        self.calc.multiply(4, 5)
        self.calc.divide(10, 2)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 3)
        self.assertIn("2 + 3 = 5", history[0])
        self.assertIn("4 × 5 = 20", history[1])
        self.assertIn("10 ÷ 2 = 5", history[2])
        
        # Clear history
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Very large numbers
        large_result = self.calc.multiply(1e10, 1e10)
        self.assertEqual(large_result, 1e20)
        
        # Very small numbers
        small_result = self.calc.divide(1, 1e10)
        self.assertEqual(small_result, 1e-10)
        
        # Zero operations
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.multiply(0, 1000), 0)
        self.assertEqual(self.calc.power(0, 5), 0)


def run_performance_test():
    """Run a simple performance test."""
    print("\n🚀 Running performance test...")
    calc = Calculator()
    
    import time
    start_time = time.time()
    
    # Perform 1000 calculations
    for i in range(1000):
        calc.add(i, i + 1)
        calc.multiply(i, 2)
        if i > 0:
            calc.divide(i * 2, i)
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    print(f"✅ Completed 3000 calculations in {elapsed:.4f} seconds")
    print(f"📊 Average time per calculation: {(elapsed/3000)*1000:.4f} ms")
    print(f"📈 History contains {len(calc.get_history())} entries")


def main():
    """Run all tests."""
    print("🧪 Running Calculator Tests")
    print("=" * 50)
    
    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Run performance test
    run_performance_test()
    
    print("\n✅ All tests completed!")
    print("Calculator program is ready to use! 🎉")


if __name__ == "__main__":
    main()
