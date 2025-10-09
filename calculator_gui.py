#!/usr/bin/env python3
"""
Calculator GUI Program
A graphical calculator using tkinter with basic and scientific operations.
Author: Codegen (for ClickUp task #86d0jt9dz)
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
from calculator import Calculator


class CalculatorGUI:
    """A graphical calculator interface using tkinter."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Calculator Program")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Initialize calculator engine
        self.calc = Calculator()
        
        # Variables
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.current_input = ""
        self.last_operation = ""
        self.result_displayed = False
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Display
        display_frame = ttk.Frame(main_frame)
        display_frame.grid(row=0, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))
        
        display = ttk.Entry(
            display_frame, 
            textvariable=self.display_var, 
            font=("Arial", 16), 
            justify="right",
            state="readonly"
        )
        display.grid(row=0, column=0, sticky=(tk.W, tk.E))
        display_frame.columnconfigure(0, weight=1)
        
        # History display
        history_frame = ttk.LabelFrame(main_frame, text="Recent Calculations", padding="5")
        history_frame.grid(row=1, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.history_text = tk.Text(history_frame, height=4, width=40, font=("Arial", 9))
        history_scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=self.history_text.yview)
        self.history_text.configure(yscrollcommand=history_scrollbar.set)
        
        self.history_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        history_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        history_frame.columnconfigure(0, weight=1)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=4, sticky=(tk.W, tk.E))
        
        # Create buttons
        self.create_buttons(button_frame)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.columnconfigure(3, weight=1)
    
    def create_buttons(self, parent):
        """Create calculator buttons."""
        # Button configuration
        button_config = {"width": 8, "height": 2}
        
        # Row 0: Clear and operations
        ttk.Button(parent, text="Clear", command=self.clear, **button_config).grid(row=0, column=0, padx=2, pady=2)
        ttk.Button(parent, text="⌫", command=self.backspace, **button_config).grid(row=0, column=1, padx=2, pady=2)
        ttk.Button(parent, text="√", command=lambda: self.scientific_operation("sqrt"), **button_config).grid(row=0, column=2, padx=2, pady=2)
        ttk.Button(parent, text="÷", command=lambda: self.operation("÷"), **button_config).grid(row=0, column=3, padx=2, pady=2)
        
        # Row 1: Numbers and operations
        ttk.Button(parent, text="7", command=lambda: self.number_click("7"), **button_config).grid(row=1, column=0, padx=2, pady=2)
        ttk.Button(parent, text="8", command=lambda: self.number_click("8"), **button_config).grid(row=1, column=1, padx=2, pady=2)
        ttk.Button(parent, text="9", command=lambda: self.number_click("9"), **button_config).grid(row=1, column=2, padx=2, pady=2)
        ttk.Button(parent, text="×", command=lambda: self.operation("×"), **button_config).grid(row=1, column=3, padx=2, pady=2)
        
        # Row 2
        ttk.Button(parent, text="4", command=lambda: self.number_click("4"), **button_config).grid(row=2, column=0, padx=2, pady=2)
        ttk.Button(parent, text="5", command=lambda: self.number_click("5"), **button_config).grid(row=2, column=1, padx=2, pady=2)
        ttk.Button(parent, text="6", command=lambda: self.number_click("6"), **button_config).grid(row=2, column=2, padx=2, pady=2)
        ttk.Button(parent, text="-", command=lambda: self.operation("-"), **button_config).grid(row=2, column=3, padx=2, pady=2)
        
        # Row 3
        ttk.Button(parent, text="1", command=lambda: self.number_click("1"), **button_config).grid(row=3, column=0, padx=2, pady=2)
        ttk.Button(parent, text="2", command=lambda: self.number_click("2"), **button_config).grid(row=3, column=1, padx=2, pady=2)
        ttk.Button(parent, text="3", command=lambda: self.number_click("3"), **button_config).grid(row=3, column=2, padx=2, pady=2)
        ttk.Button(parent, text="+", command=lambda: self.operation("+"), **button_config).grid(row=3, column=3, padx=2, pady=2)
        
        # Row 4
        ttk.Button(parent, text="0", command=lambda: self.number_click("0"), **button_config).grid(row=4, column=0, padx=2, pady=2)
        ttk.Button(parent, text=".", command=lambda: self.number_click("."), **button_config).grid(row=4, column=1, padx=2, pady=2)
        ttk.Button(parent, text="^", command=lambda: self.operation("^"), **button_config).grid(row=4, column=2, padx=2, pady=2)
        ttk.Button(parent, text="=", command=self.calculate, **button_config).grid(row=4, column=3, padx=2, pady=2)
        
        # Row 5: Scientific functions
        ttk.Button(parent, text="sin", command=lambda: self.scientific_operation("sin"), **button_config).grid(row=5, column=0, padx=2, pady=2)
        ttk.Button(parent, text="cos", command=lambda: self.scientific_operation("cos"), **button_config).grid(row=5, column=1, padx=2, pady=2)
        ttk.Button(parent, text="tan", command=lambda: self.scientific_operation("tan"), **button_config).grid(row=5, column=2, padx=2, pady=2)
        ttk.Button(parent, text="log", command=lambda: self.scientific_operation("log"), **button_config).grid(row=5, column=3, padx=2, pady=2)
        
        # Row 6: More functions
        ttk.Button(parent, text="π", command=lambda: self.number_click(str(math.pi)), **button_config).grid(row=6, column=0, padx=2, pady=2)
        ttk.Button(parent, text="e", command=lambda: self.number_click(str(math.e)), **button_config).grid(row=6, column=1, padx=2, pady=2)
        ttk.Button(parent, text="n!", command=lambda: self.scientific_operation("factorial"), **button_config).grid(row=6, column=2, padx=2, pady=2)
        ttk.Button(parent, text="History", command=self.show_history, **button_config).grid(row=6, column=3, padx=2, pady=2)
    
    def number_click(self, number):
        """Handle number button clicks."""
        if self.result_displayed:
            self.current_input = ""
            self.result_displayed = False
        
        if number == "." and "." in self.current_input:
            return  # Prevent multiple decimal points
        
        self.current_input += number
        self.display_var.set(self.current_input)
    
    def operation(self, op):
        """Handle operation button clicks."""
        if self.current_input:
            if self.last_operation and not self.result_displayed:
                self.calculate()
            
            self.last_operation = f"{self.current_input} {op} "
            self.current_input = ""
            self.result_displayed = False
    
    def scientific_operation(self, func):
        """Handle scientific operation button clicks."""
        if not self.current_input:
            messagebox.showerror("Error", "Please enter a number first!")
            return
        
        try:
            value = float(self.current_input)
            
            if func == "sqrt":
                result = self.calc.square_root(value)
            elif func == "sin":
                result = self.calc.sin(value, degrees=True)  # Default to degrees for GUI
            elif func == "cos":
                result = self.calc.cos(value, degrees=True)
            elif func == "tan":
                result = self.calc.tan(value, degrees=True)
            elif func == "log":
                result = self.calc.log(value)
            elif func == "factorial":
                if value != int(value) or value < 0:
                    messagebox.showerror("Error", "Factorial requires a non-negative integer!")
                    return
                result = self.calc.factorial(int(value))
            else:
                return
            
            self.display_var.set(str(result))
            self.current_input = str(result)
            self.result_displayed = True
            self.update_history()
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def calculate(self):
        """Perform the calculation."""
        if not self.last_operation or not self.current_input:
            return
        
        try:
            # Parse the operation
            parts = self.last_operation.strip().split()
            if len(parts) < 2:
                return
            
            first_num = float(parts[0])
            operator = parts[1]
            second_num = float(self.current_input)
            
            # Perform calculation using Calculator class
            if operator == "+":
                result = self.calc.add(first_num, second_num)
            elif operator == "-":
                result = self.calc.subtract(first_num, second_num)
            elif operator == "×":
                result = self.calc.multiply(first_num, second_num)
            elif operator == "÷":
                result = self.calc.divide(first_num, second_num)
            elif operator == "^":
                result = self.calc.power(first_num, second_num)
            else:
                return
            
            self.display_var.set(str(result))
            self.current_input = str(result)
            self.last_operation = ""
            self.result_displayed = True
            self.update_history()
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def clear(self):
        """Clear the calculator."""
        self.current_input = ""
        self.last_operation = ""
        self.display_var.set("0")
        self.result_displayed = False
    
    def backspace(self):
        """Remove the last character."""
        if self.current_input and not self.result_displayed:
            self.current_input = self.current_input[:-1]
            self.display_var.set(self.current_input if self.current_input else "0")
    
    def update_history(self):
        """Update the history display."""
        history = self.calc.get_history()
        if history:
            # Show last 3 calculations
            recent = history[-3:]
            self.history_text.delete(1.0, tk.END)
            for calculation in recent:
                self.history_text.insert(tk.END, calculation + "\n")
            self.history_text.see(tk.END)
    
    def show_history(self):
        """Show full calculation history in a new window."""
        history = self.calc.get_history()
        if not history:
            messagebox.showinfo("History", "No calculations in history yet.")
            return
        
        # Create history window
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("400x300")
        
        # History text widget with scrollbar
        text_frame = ttk.Frame(history_window, padding="10")
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        history_text = tk.Text(text_frame, wrap=tk.WORD, font=("Arial", 10))
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=history_text.yview)
        history_text.configure(yscrollcommand=scrollbar.set)
        
        history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add history to text widget
        for i, calculation in enumerate(history, 1):
            history_text.insert(tk.END, f"{i:2d}. {calculation}\n")
        
        history_text.config(state=tk.DISABLED)
        
        # Clear history button
        button_frame = ttk.Frame(history_window, padding="10")
        button_frame.pack(fill=tk.X)
        
        def clear_history():
            self.calc.clear_history()
            self.history_text.delete(1.0, tk.END)
            history_window.destroy()
            messagebox.showinfo("History", "History cleared!")
        
        ttk.Button(button_frame, text="Clear History", command=clear_history).pack()


def main():
    """Main function to run the GUI calculator."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    
    # Add some styling
    style = ttk.Style()
    style.theme_use('clam')  # Use a modern theme
    
    print("🎉 Calculator GUI started!")
    print("Created for ClickUp task #86d0jt9dz")
    
    root.mainloop()


if __name__ == "__main__":
    main()
