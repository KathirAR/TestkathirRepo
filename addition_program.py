#!/usr/bin/env python3
"""
Addition Program
Author: Kathir (via Codegen)

A comprehensive addition program that supports:
- Basic addition of two numbers
- Addition of multiple numbers
- Interactive command-line interface
- Input validation and error handling
"""

import sys
from typing import List, Union


def add_two_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    return a + b


def add_multiple_numbers(numbers: List[float]) -> float:
    """
    Add multiple numbers together.
    
    Args:
        numbers (List[float]): List of numbers to add
    
    Returns:
        float: Sum of all numbers
    """
    return sum(numbers)


def get_number_input(prompt: str) -> float:
    """
    Get a valid number input from the user.
    
    Args:
        prompt (str): Prompt message to display
    
    Returns:
        float: Valid number entered by user
    
    Raises:
        KeyboardInterrupt: If user cancels input
    """
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            sys.exit(0)


def get_multiple_numbers() -> List[float]:
    """
    Get multiple numbers from user input.
    
    Returns:
        List[float]: List of numbers entered by user
    """
    numbers = []
    print("\n📝 Enter numbers to add (press Enter with empty input to finish):")
    
    count = 1
    while True:
        try:
            value = input(f"Number {count}: ")
            if value.strip() == "":
                break
            numbers.append(float(value))
            count += 1
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            sys.exit(0)
    
    return numbers


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("🧮 ADDITION PROGRAM")
    print("="*50)
    print("1. Add two numbers")
    print("2. Add multiple numbers")
    print("3. Quick calculation (command line)")
    print("4. Exit")
    print("="*50)


def quick_calculation():
    """Handle quick calculation from command line arguments."""
    if len(sys.argv) < 3:
        print("❌ Usage: python addition_program.py <number1> <number2> [number3] ...")
        return
    
    try:
        numbers = [float(arg) for arg in sys.argv[1:]]
        result = add_multiple_numbers(numbers)
        
        print(f"\n🧮 Quick Calculation:")
        print(f"Numbers: {' + '.join(map(str, numbers))}")
        print(f"Result: {result}")
        
    except ValueError:
        print("❌ Error: All arguments must be valid numbers!")


def main():
    """Main program function."""
    # Check if command line arguments are provided for quick calculation
    if len(sys.argv) > 1:
        quick_calculation()
        return
    
    print("🎉 Welcome to the Addition Program!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\n🔢 Enter your choice (1-4): ").strip()
            
            if choice == "1":
                print("\n➕ Adding Two Numbers")
                print("-" * 25)
                
                num1 = get_number_input("Enter first number: ")
                num2 = get_number_input("Enter second number: ")
                
                result = add_two_numbers(num1, num2)
                
                print(f"\n✅ Result: {num1} + {num2} = {result}")
                
            elif choice == "2":
                print("\n➕ Adding Multiple Numbers")
                print("-" * 30)
                
                numbers = get_multiple_numbers()
                
                if not numbers:
                    print("❌ No numbers entered!")
                    continue
                
                result = add_multiple_numbers(numbers)
                
                print(f"\n✅ Result: {' + '.join(map(str, numbers))} = {result}")
                print(f"📊 Total numbers added: {len(numbers)}")
                
            elif choice == "3":
                print("\n⚡ Quick Calculation Mode")
                print("-" * 30)
                print("Usage: python addition_program.py <number1> <number2> [number3] ...")
                print("Example: python addition_program.py 5 10 15")
                
            elif choice == "4":
                print("\n👋 Thank you for using the Addition Program!")
                print("Goodbye! 🎉")
                break
                
            else:
                print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
