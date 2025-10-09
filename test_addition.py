#!/usr/bin/env python3
"""
Test file for the Addition Program
Author: Kathir (via Codegen)

Simple tests to verify the addition program functions work correctly.
"""

from addition_program import add_two_numbers, add_multiple_numbers


def test_add_two_numbers():
    """Test the add_two_numbers function."""
    print("🧪 Testing add_two_numbers function...")
    
    # Test cases
    test_cases = [
        (5, 3, 8),
        (10.5, 2.5, 13.0),
        (-5, 10, 5),
        (0, 0, 0),
        (-3, -7, -10)
    ]
    
    for a, b, expected in test_cases:
        result = add_two_numbers(a, b)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"  {a} + {b} = {result} (expected {expected}) {status}")


def test_add_multiple_numbers():
    """Test the add_multiple_numbers function."""
    print("\n🧪 Testing add_multiple_numbers function...")
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 15),
        ([10.5, 2.5, 7.0], 20.0),
        ([-5, 10, -3], 2),
        ([0], 0),
        ([100], 100),
        ([], 0)
    ]
    
    for numbers, expected in test_cases:
        result = add_multiple_numbers(numbers)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"  {numbers} = {result} (expected {expected}) {status}")


def main():
    """Run all tests."""
    print("🎯 Running Addition Program Tests")
    print("=" * 40)
    
    test_add_two_numbers()
    test_add_multiple_numbers()
    
    print("\n🎉 All tests completed!")


if __name__ == "__main__":
    main()
