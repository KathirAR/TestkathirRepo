#!/usr/bin/env python3
"""
Test script for the basic calculator program
"""

# Import the calculator functions
from calculator import add, subtract, multiply, divide, power

def test_calculator():
    """Test all calculator functions"""
    print("Testing Basic Calculator Functions:")
    print("=" * 40)
    
    # Test addition
    result = add(5, 3)
    print(f"add(5, 3) = {result}")
    assert result == 8, "Addition test failed"
    
    # Test subtraction
    result = subtract(10, 4)
    print(f"subtract(10, 4) = {result}")
    assert result == 6, "Subtraction test failed"
    
    # Test multiplication
    result = multiply(6, 7)
    print(f"multiply(6, 7) = {result}")
    assert result == 42, "Multiplication test failed"
    
    # Test division
    result = divide(15, 3)
    print(f"divide(15, 3) = {result}")
    assert result == 5.0, "Division test failed"
    
    # Test division by zero
    result = divide(10, 0)
    print(f"divide(10, 0) = {result}")
    assert "Error" in str(result), "Division by zero test failed"
    
    # Test power
    result = power(2, 3)
    print(f"power(2, 3) = {result}")
    assert result == 8, "Power test failed"
    
    print("=" * 40)
    print("✅ All tests passed! Calculator is working correctly.")

if __name__ == "__main__":
    test_calculator()
