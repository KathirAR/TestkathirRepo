#!/usr/bin/env python3
"""
Addition Program
A simple program that demonstrates addition operations.

Author: Kathir (via Codegen)
Created for ClickUp task: "Addition" program
"""

def add_two_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    return a + b

def add_multiple_numbers(*numbers):
    """
    Add multiple numbers and return the result.
    
    Args:
        *numbers: Variable number of numeric arguments
    
    Returns:
        float: Sum of all numbers
    """
    return sum(numbers)

def interactive_addition():
    """
    Interactive addition program that asks user for input.
    """
    print("🧮 Welcome to the Addition Program! 🧮")
    print("=" * 40)
    
    try:
        # Get number of values to add
        count = int(input("How many numbers would you like to add? "))
        
        if count < 1:
            print("Please enter at least 1 number.")
            return
        
        numbers = []
        for i in range(count):
            while True:
                try:
                    num = float(input(f"Enter number {i + 1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Please enter a valid number.")
        
        # Calculate the sum
        result = add_multiple_numbers(*numbers)
        
        # Display the result
        print("\n" + "=" * 40)
        print(f"Numbers entered: {', '.join(map(str, numbers))}")
        print(f"Sum: {result}")
        print("=" * 40)
        
    except ValueError:
        print("Please enter a valid number for the count.")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye! 👋")

def demo_addition():
    """
    Demonstrate various addition operations.
    """
    print("🔢 Addition Program Demo 🔢")
    print("=" * 30)
    
    # Demo 1: Simple addition
    a, b = 5, 3
    result1 = add_two_numbers(a, b)
    print(f"Demo 1: {a} + {b} = {result1}")
    
    # Demo 2: Decimal addition
    c, d = 2.5, 3.7
    result2 = add_two_numbers(c, d)
    print(f"Demo 2: {c} + {d} = {result2}")
    
    # Demo 3: Multiple numbers
    numbers = [1, 2, 3, 4, 5]
    result3 = add_multiple_numbers(*numbers)
    print(f"Demo 3: {' + '.join(map(str, numbers))} = {result3}")
    
    # Demo 4: Negative numbers
    e, f = -10, 15
    result4 = add_two_numbers(e, f)
    print(f"Demo 4: {e} + {f} = {result4}")
    
    print("=" * 30)

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Run interactive addition")
    print("2. Run demo")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == "1":
        interactive_addition()
    elif choice == "2":
        demo_addition()
    elif choice == "3":
        print("Goodbye! 👋")
    else:
        print("Invalid choice. Running demo instead...")
        demo_addition()
