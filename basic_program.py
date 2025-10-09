#!/usr/bin/env python3
"""
Basic Program - A simple Python program demonstrating fundamental programming concepts
Created for ClickUp task: Any basic program
Author: Codegen
"""

def greet_user(name):
    """Function to greet a user with their name"""
    return f"Hello, {name}! Welcome to our basic program! 👋"

def calculate_area(length, width):
    """Function to calculate the area of a rectangle"""
    return length * width

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms"""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    """Main function that demonstrates the program functionality"""
    print("=" * 50)
    print("🚀 BASIC PROGRAM DEMONSTRATION")
    print("=" * 50)
    
    # User greeting
    user_name = "Kathir"
    greeting = greet_user(user_name)
    print(f"\n1. {greeting}")
    
    # Rectangle area calculation
    length, width = 10, 5
    area = calculate_area(length, width)
    print(f"\n2. 📐 Rectangle Area Calculation:")
    print(f"   Length: {length}, Width: {width}")
    print(f"   Area: {area} square units")
    
    # Fibonacci sequence
    n_terms = 8
    fib_sequence = fibonacci_sequence(n_terms)
    print(f"\n3. 🔢 Fibonacci Sequence (first {n_terms} terms):")
    print(f"   {fib_sequence}")
    
    # Simple loop demonstration
    print(f"\n4. 🔄 Loop Demonstration:")
    print("   Counting from 1 to 5:")
    for i in range(1, 6):
        print(f"   Count: {i}")
    
    # Basic conditional logic
    print(f"\n5. 🤔 Conditional Logic:")
    numbers = [15, 8, 23, 4, 42]
    print(f"   Numbers: {numbers}")
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    print(f"   Even numbers: {even_numbers}")
    print(f"   Odd numbers: {odd_numbers}")
    
    print(f"\n{'=' * 50}")
    print("✅ Program completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()
