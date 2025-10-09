#!/usr/bin/env python3
"""
Calculator Program
A comprehensive calculator with basic arithmetic operations, scientific functions,
and both CLI and GUI interfaces.
"""

import math
import sys
from typing import Union

class Calculator:
    """A comprehensive calculator class with basic and scientific operations."""
    
    def __init__(self):
        self.history = []
        self.memory = 0
    
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
    
    def square_root(self, x: float) -> float:
        """Calculate square root of x."""
        if x < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(x)
        self._add_to_history(f"√{x} = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Calculate factorial of n."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        if n > 170:  # Prevent overflow
            raise ValueError("Number too large for factorial calculation!")
        result = math.factorial(n)
        self._add_to_history(f"{n}! = {result}")
        return result
    
    def sin(self, x: float, degrees: bool = False) -> float:
        """Calculate sine of x (in radians by default)."""
        if degrees:
            x = math.radians(x)
        result = math.sin(x)
        unit = "°" if degrees else " rad"
        self._add_to_history(f"sin({x}{unit}) = {result}")
        return result
    
    def cos(self, x: float, degrees: bool = False) -> float:
        """Calculate cosine of x (in radians by default)."""
        if degrees:
            x = math.radians(x)
        result = math.cos(x)
        unit = "°" if degrees else " rad"
        self._add_to_history(f"cos({x}{unit}) = {result}")
        return result
    
    def tan(self, x: float, degrees: bool = False) -> float:
        """Calculate tangent of x (in radians by default)."""
        if degrees:
            x = math.radians(x)
        result = math.tan(x)
        unit = "°" if degrees else " rad"
        self._add_to_history(f"tan({x}{unit}) = {result}")
        return result
    
    def log(self, x: float, base: float = math.e) -> float:
        """Calculate logarithm of x with given base (natural log by default)."""
        if x <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers!")
        if base <= 0 or base == 1:
            raise ValueError("Invalid logarithm base!")
        
        if base == math.e:
            result = math.log(x)
            self._add_to_history(f"ln({x}) = {result}")
        elif base == 10:
            result = math.log10(x)
            self._add_to_history(f"log₁₀({x}) = {result}")
        else:
            result = math.log(x, base)
            self._add_to_history(f"log_{base}({x}) = {result}")
        return result
    
    def memory_store(self, value: float) -> None:
        """Store value in memory."""
        self.memory = value
        self._add_to_history(f"Memory stored: {value}")
    
    def memory_recall(self) -> float:
        """Recall value from memory."""
        self._add_to_history(f"Memory recalled: {self.memory}")
        return self.memory
    
    def memory_clear(self) -> None:
        """Clear memory."""
        self.memory = 0
        self._add_to_history("Memory cleared")
    
    def get_history(self) -> list:
        """Get calculation history."""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()
    
    def _add_to_history(self, operation: str) -> None:
        """Add operation to history."""
        self.history.append(operation)
        if len(self.history) > 100:  # Keep only last 100 operations
            self.history.pop(0)


def print_menu():
    """Print the calculator menu."""
    print("\n" + "="*50)
    print("🧮 CALCULATOR PROGRAM")
    print("="*50)
    print("Basic Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (×)")
    print("  4. Division (÷)")
    print("  5. Power (^)")
    print("  6. Square Root (√)")
    print("\nScientific Operations:")
    print("  7. Factorial (!)")
    print("  8. Sine (sin)")
    print("  9. Cosine (cos)")
    print(" 10. Tangent (tan)")
    print(" 11. Natural Logarithm (ln)")
    print(" 12. Logarithm base 10 (log₁₀)")
    print("\nMemory Operations:")
    print(" 13. Store in Memory (MS)")
    print(" 14. Recall from Memory (MR)")
    print(" 15. Clear Memory (MC)")
    print("\nUtility:")
    print(" 16. Show History")
    print(" 17. Clear History")
    print("  0. Exit")
    print("="*50)


def get_number(prompt: str) -> float:
    """Get a number from user input with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def get_integer(prompt: str) -> int:
    """Get an integer from user input with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.")


def main():
    """Main calculator program."""
    calc = Calculator()
    
    print("🎉 Welcome to the Calculator Program!")
    print("This calculator supports basic arithmetic and scientific operations.")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (0-17): ").strip()
            
            if choice == '0':
                print("\n👋 Thank you for using the Calculator! Goodbye!")
                break
            
            elif choice == '1':  # Addition
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                print(f"✅ Result: {a} + {b} = {result}")
            
            elif choice == '2':  # Subtraction
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                print(f"✅ Result: {a} - {b} = {result}")
            
            elif choice == '3':  # Multiplication
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.multiply(a, b)
                print(f"✅ Result: {a} × {b} = {result}")
            
            elif choice == '4':  # Division
                a = get_number("Enter dividend: ")
                b = get_number("Enter divisor: ")
                try:
                    result = calc.divide(a, b)
                    print(f"✅ Result: {a} ÷ {b} = {result}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            
            elif choice == '5':  # Power
                base = get_number("Enter base: ")
                exponent = get_number("Enter exponent: ")
                result = calc.power(base, exponent)
                print(f"✅ Result: {base} ^ {exponent} = {result}")
            
            elif choice == '6':  # Square Root
                x = get_number("Enter number: ")
                try:
                    result = calc.square_root(x)
                    print(f"✅ Result: √{x} = {result}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            
            elif choice == '7':  # Factorial
                n = get_integer("Enter integer: ")
                try:
                    result = calc.factorial(n)
                    print(f"✅ Result: {n}! = {result}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            
            elif choice == '8':  # Sine
                x = get_number("Enter angle: ")
                degrees = input("Use degrees? (y/n): ").lower().startswith('y')
                result = calc.sin(x, degrees)
                unit = "°" if degrees else " radians"
                print(f"✅ Result: sin({x}{unit}) = {result}")
            
            elif choice == '9':  # Cosine
                x = get_number("Enter angle: ")
                degrees = input("Use degrees? (y/n): ").lower().startswith('y')
                result = calc.cos(x, degrees)
                unit = "°" if degrees else " radians"
                print(f"✅ Result: cos({x}{unit}) = {result}")
            
            elif choice == '10':  # Tangent
                x = get_number("Enter angle: ")
                degrees = input("Use degrees? (y/n): ").lower().startswith('y')
                result = calc.tan(x, degrees)
                unit = "°" if degrees else " radians"
                print(f"✅ Result: tan({x}{unit}) = {result}")
            
            elif choice == '11':  # Natural Logarithm
                x = get_number("Enter number: ")
                try:
                    result = calc.log(x)
                    print(f"✅ Result: ln({x}) = {result}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            
            elif choice == '12':  # Logarithm base 10
                x = get_number("Enter number: ")
                try:
                    result = calc.log(x, 10)
                    print(f"✅ Result: log₁₀({x}) = {result}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            
            elif choice == '13':  # Memory Store
                value = get_number("Enter value to store: ")
                calc.memory_store(value)
                print(f"✅ Value {value} stored in memory")
            
            elif choice == '14':  # Memory Recall
                value = calc.memory_recall()
                print(f"✅ Memory value: {value}")
            
            elif choice == '15':  # Memory Clear
                calc.memory_clear()
                print("✅ Memory cleared")
            
            elif choice == '16':  # Show History
                history = calc.get_history()
                if history:
                    print("\n📜 Calculation History:")
                    print("-" * 30)
                    for i, operation in enumerate(history[-10:], 1):  # Show last 10
                        print(f"{i:2d}. {operation}")
                    if len(history) > 10:
                        print(f"... and {len(history) - 10} more operations")
                else:
                    print("📜 No calculations in history yet.")
            
            elif choice == '17':  # Clear History
                calc.clear_history()
                print("✅ History cleared")
            
            else:
                print("❌ Invalid choice! Please select a number from 0-17.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Calculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
