#!/usr/bin/env python3
"""
Basic Calculator Program
A simple calculator that performs basic arithmetic operations.

Author: Codegen (for ClickUp task #86d0jt8rc)
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def power(x, y):
    """Raise x to the power of y"""
    return x ** y

def display_menu():
    """Display the calculator menu"""
    print("\n🧮 Basic Calculator")
    print("=" * 20)
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Exit")
    print("=" * 20)

def get_numbers():
    """Get two numbers from user input"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def main():
    """Main calculator function"""
    print("Welcome to the Basic Calculator! 🎉")
    
    while True:
        display_menu()
        
        try:
            choice = input("Select operation (1-6): ").strip()
            
            if choice == '6':
                print("Thank you for using the calculator! Goodbye! 👋")
                break
            
            if choice not in ['1', '2', '3', '4', '5']:
                print("Error: Invalid choice! Please select 1-6.")
                continue
            
            num1, num2 = get_numbers()
            if num1 is None or num2 is None:
                continue
            
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            elif choice == '5':
                result = power(num1, num2)
                operation = "^"
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
            
            # Ask if user wants to continue
            continue_calc = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
            if continue_calc not in ['y', 'yes']:
                print("Thank you for using the calculator! Goodbye! 👋")
                break
                
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye! 👋")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
