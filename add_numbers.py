#!/usr/bin/env python3
"""
Simple module for adding two numbers.
This module provides a function to add two numbers together.
"""

def add_two_numbers(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of the two numbers
    
    Examples:
        >>> add_two_numbers(5, 3)
        8
        >>> add_two_numbers(2.5, 1.5)
        4.0
    """
    return a + b


def main():
    """
    Main function to demonstrate the addition functionality.
    """
    # Example usage
    num1 = 10
    num2 = 25
    result = add_two_numbers(num1, num2)
    
    print(f"Adding {num1} + {num2} = {result}")
    
    # Interactive example
    try:
        user_num1 = float(input("Enter first number: "))
        user_num2 = float(input("Enter second number: "))
        user_result = add_two_numbers(user_num1, user_num2)
        print(f"Result: {user_num1} + {user_num2} = {user_result}")
    except ValueError:
        print("Please enter valid numbers!")


if __name__ == "__main__":
    main()

