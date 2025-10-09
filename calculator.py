#!/usr/bin/env python3
"""
Calculator Program
A comprehensive calculator with basic arithmetic operations, scientific functions, and history tracking.
Author: Codegen (for ClickUp task #86d0jt9dz)
"""

import math
import sys
from typing import List, Union


class Calculator:
    """A comprehensive calculator class with history tracking."""
    
    def __init__(self):
        self.history: List[str] = []
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        result = a * b
        self._add_to_history(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self._add_to_history(f"{a} ÷ {b} = {result}")
        return result
    
    def power(self, base: float, exponent: float) -> float:
        """Raise base to the power of exponent."""
        result = base ** exponent
        self._add_to_history(f"{base} ^ {exponent} = {result}")
        return result
    
    def square_root(self, n: float) -> float:
        """Calculate square root of n."""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(n)
        self._add_to_history(f"√{n} = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Calculate factorial of n."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        if not isinstance(n, int):
            raise ValueError("Factorial requires an integer!")
        result = math.factorial(n)
        self._add_to_history(f"{n}! = {result}")
        return result
    
    def sin(self, angle: float, degrees: bool = False) -> float:
        """Calculate sine of angle (in radians by default)."""
        if degrees:
            angle = math.radians(angle)
        result = math.sin(angle)
        unit = "°" if degrees else " rad"
        self._add_to_history(f"sin({angle}{unit}) = {result}")
        return result
    
    def cos(self, angle: float, degrees: bool = False) -> float:
        """Calculate cosine of angle (in radians by default)."""
        if degrees:
            angle = math.radians(angle)
        result = math.cos(angle)
        unit = "°" if degrees else " rad"
        self._add_to_history(f"cos({angle}{unit}) = {result}")
        return result
    
    def tan(self, angle: float, degrees: bool = False) -> float:
        """Calculate tangent of angle (in radians by default)."""
        if degrees:
            angle = math.radians(angle)
        result = math.tan(angle)
        unit = "°" if degrees else " rad"
        self._add_to_history(f"tan({angle}{unit}) = {result}")
        return result
    
    def log(self, n: float, base: float = math.e) -> float:
        """Calculate logarithm of n with given base (natural log by default)."""
        if n <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers!")
        if base <= 0 or base == 1:
            raise ValueError("Invalid logarithm base!")
        
        if base == math.e:
            result = math.log(n)
            self._add_to_history(f"ln({n}) = {result}")
        else:
            result = math.log(n, base)
            self._add_to_history(f"log_{base}({n}) = {result}")
        return result
    
    def percentage(self, value: float, percent: float) -> float:
        """Calculate percentage of a value."""
        result = (percent / 100) * value
        self._add_to_history(f"{percent}% of {value} = {result}")
        return result
    
    def _add_to_history(self, operation: str):
        """Add operation to history."""
        self.history.append(operation)
    
    def get_history(self) -> List[str]:
        """Get calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
    
    def evaluate_expression(self, expression: str) -> float:
        """Safely evaluate a mathematical expression."""
        # Remove spaces and replace common symbols
        expression = expression.replace(" ", "")
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        expression = expression.replace("^", "**")
        
        # Only allow safe characters and functions
        allowed_chars = set("0123456789+-*/.()e")
        allowed_functions = ["sin", "cos", "tan", "log", "sqrt", "abs", "round"]
        
        # Basic security check
        if not all(c in allowed_chars or c.isalpha() for c in expression):
            raise ValueError("Invalid characters in expression!")
        
        try:
            # Create a safe namespace for evaluation
            safe_dict = {
                "__builtins__": {},
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log,
                "sqrt": math.sqrt,
                "abs": abs,
                "round": round,
                "pi": math.pi,
                "e": math.e
            }
            
            result = eval(expression, safe_dict)
            self._add_to_history(f"{expression} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")


def print_menu():
    """Print the calculator menu."""
    print("\n" + "="*50)
    print("🧮 CALCULATOR PROGRAM")
    print("="*50)
    print("1.  Addition (+)")
    print("2.  Subtraction (-)")
    print("3.  Multiplication (×)")
    print("4.  Division (÷)")
    print("5.  Power (^)")
    print("6.  Square Root (√)")
    print("7.  Factorial (!)")
    print("8.  Sine")
    print("9.  Cosine")
    print("10. Tangent")
    print("11. Logarithm")
    print("12. Percentage")
    print("13. Expression Evaluator")
    print("14. View History")
    print("15. Clear History")
    print("0.  Exit")
    print("="*50)


def get_number(prompt: str) -> float:
    """Get a number from user input with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")


def get_integer(prompt: str) -> int:
    """Get an integer from user input with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid integer!")


def main():
    """Main calculator program."""
    calc = Calculator()
    
    print("🎉 Welcome to the Calculator Program!")
    print("Created for ClickUp task #86d0jt9dz")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (0-15): ").strip()
            
            if choice == "0":
                print("👋 Thank you for using the calculator! Goodbye!")
                break
            
            elif choice == "1":  # Addition
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                print(f"✅ Result: {a} + {b} = {result}")
            
            elif choice == "2":  # Subtraction
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                print(f"✅ Result: {a} - {b} = {result}")
            
            elif choice == "3":  # Multiplication
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.multiply(a, b)
                print(f"✅ Result: {a} × {b} = {result}")
            
            elif choice == "4":  # Division
                a = get_number("Enter dividend: ")
                b = get_number("Enter divisor: ")
                try:
                    result = calc.divide(a, b)
                    print(f"✅ Result: {a} ÷ {b} = {result}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            
            elif choice == "5":  # Power
                base = get_number("Enter base: ")
                exponent = get_number("Enter exponent: ")
                result = calc.power(base, exponent)
                print(f"✅ Result: {base} ^ {exponent} = {result}")
            
            elif choice == "6":  # Square Root
                n = get_number("Enter number: ")
                try:
                    result = calc.square_root(n)
                    print(f"✅ Result: √{n} = {result}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            
            elif choice == "7":  # Factorial
                n = get_integer("Enter integer: ")
                try:
                    result = calc.factorial(n)
                    print(f"✅ Result: {n}! = {result}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            
            elif choice == "8":  # Sine
                angle = get_number("Enter angle: ")
                degrees = input("Is the angle in degrees? (y/n): ").lower().startswith('y')
                result = calc.sin(angle, degrees)
                unit = "°" if degrees else " radians"
                print(f"✅ Result: sin({angle}{unit}) = {result}")
            
            elif choice == "9":  # Cosine
                angle = get_number("Enter angle: ")
                degrees = input("Is the angle in degrees? (y/n): ").lower().startswith('y')
                result = calc.cos(angle, degrees)
                unit = "°" if degrees else " radians"
                print(f"✅ Result: cos({angle}{unit}) = {result}")
            
            elif choice == "10":  # Tangent
                angle = get_number("Enter angle: ")
                degrees = input("Is the angle in degrees? (y/n): ").lower().startswith('y')
                result = calc.tan(angle, degrees)
                unit = "°" if degrees else " radians"
                print(f"✅ Result: tan({angle}{unit}) = {result}")
            
            elif choice == "11":  # Logarithm
                n = get_number("Enter number: ")
                base_input = input("Enter base (press Enter for natural log): ").strip()
                try:
                    if base_input:
                        base = float(base_input)
                        result = calc.log(n, base)
                    else:
                        result = calc.log(n)
                    print(f"✅ Result: {result}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            
            elif choice == "12":  # Percentage
                value = get_number("Enter value: ")
                percent = get_number("Enter percentage: ")
                result = calc.percentage(value, percent)
                print(f"✅ Result: {percent}% of {value} = {result}")
            
            elif choice == "13":  # Expression Evaluator
                expression = input("Enter mathematical expression: ")
                try:
                    result = calc.evaluate_expression(expression)
                    print(f"✅ Result: {expression} = {result}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            
            elif choice == "14":  # View History
                history = calc.get_history()
                if history:
                    print("\n📊 CALCULATION HISTORY:")
                    print("-" * 30)
                    for i, operation in enumerate(history, 1):
                        print(f"{i:2d}. {operation}")
                else:
                    print("📝 No calculations in history yet.")
            
            elif choice == "15":  # Clear History
                calc.clear_history()
                print("🗑️ History cleared!")
            
            else:
                print("❌ Invalid choice! Please select a number from 0-15.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
