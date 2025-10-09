#!/usr/bin/env python3
"""
Calculator GUI Program
A graphical user interface for the calculator using tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
from calculator import Calculator


class CalculatorGUI:
    """A GUI calculator application using tkinter."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Initialize calculator engine
        self.calc = Calculator()
        
        # Variables
        self.display_var = tk.StringVar(value="0")
        self.current_input = ""
        self.operation = None
        self.first_number = None
        self.waiting_for_operand = False
        
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
        
        # Button style
        style = ttk.Style()
        style.configure("Calc.TButton", font=("Arial", 12), padding=5)
        style.configure("Op.TButton", font=("Arial", 12, "bold"), padding=5)
        style.configure("Func.TButton", font=("Arial", 10), padding=3)
        
        # Memory and function buttons row
        ttk.Button(main_frame, text="MC", command=self.memory_clear, 
                  style="Func.TButton").grid(row=1, column=0, sticky=(tk.W, tk.E), padx=1, pady=1)
        ttk.Button(main_frame, text="MR", command=self.memory_recall, 
                  style="Func.TButton").grid(row=1, column=1, sticky=(tk.W, tk.E), padx=1, pady=1)
        ttk.Button(main_frame, text="MS", command=self.memory_store, 
                  style="Func.TButton").grid(row=1, column=2, sticky=(tk.W, tk.E), padx=1, pady=1)
        ttk.Button(main_frame, text="C", command=self.clear, 
                  style="Op.TButton").grid(row=1, column=3, sticky=(tk.W, tk.E), padx=1, pady=1)
        
        # Scientific function buttons row
        ttk.Button(main_frame, text="√", command=self.square_root, 
                  style="Func.TButton").grid(row=2, column=0, sticky=(tk.W, tk.E), padx=1, pady=1)
        ttk.Button(main_frame, text="x²", command=self.square, 
                  style="Func.TButton").grid(row=2, column=1, sticky=(tk.W, tk.E), padx=1, pady=1)
        ttk.Button(main_frame, text="x!", command=self.factorial, 
                  style="Func.TButton").grid(row=2, column=2, sticky=(tk.W, tk.E), padx=1, pady=1)
        ttk.Button(main_frame, text="±", command=self.negate, 
                  style="Func.TButton").grid(row=2, column=3, sticky=(tk.W, tk.E), padx=1, pady=1)
        
        # Number and operation buttons
        buttons = [
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('÷', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('×', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3),
            ('0', 6, 0), ('.', 6, 1), ('=', 6, 2), ('+', 6, 3),
        ]
        
        for (text, row, col) in buttons:
            if text.isdigit() or text == '.':
                cmd = lambda t=text: self.input_digit(t)
                style_name = "Calc.TButton"
            elif text == '=':
                cmd = self.calculate
                style_name = "Op.TButton"
            else:
                cmd = lambda t=text: self.input_operation(t)
                style_name = "Op.TButton"
            
            if text == '0':
                ttk.Button(main_frame, text=text, command=cmd, 
                          style=style_name).grid(row=row, column=col, columnspan=2, 
                                                sticky=(tk.W, tk.E), padx=1, pady=1)
            elif text == '=':
                ttk.Button(main_frame, text=text, command=cmd, 
                          style=style_name).grid(row=row, column=col, 
                                                sticky=(tk.W, tk.E), padx=1, pady=1)
            else:
                ttk.Button(main_frame, text=text, command=cmd, 
                          style=style_name).grid(row=row, column=col, 
                                                sticky=(tk.W, tk.E), padx=1, pady=1)
        
        # History button
        ttk.Button(main_frame, text="History", command=self.show_history, 
                  style="Func.TButton").grid(row=7, column=0, columnspan=4, 
                                            sticky=(tk.W, tk.E), padx=1, pady=5)
        
        # Configure grid weights
        for i in range(4):
            main_frame.columnconfigure(i, weight=1)
    
    def input_digit(self, digit):
        """Handle digit input."""
        if self.waiting_for_operand:
            self.current_input = digit
            self.waiting_for_operand = False
        else:
            if self.current_input == "0" and digit != ".":
                self.current_input = digit
            else:
                self.current_input += digit
        
        self.display_var.set(self.current_input)
    
    def input_operation(self, op):
        """Handle operation input."""
        if self.current_input:
            if self.first_number is not None and self.operation and not self.waiting_for_operand:
                self.calculate()
            
            self.first_number = float(self.current_input)
            self.operation = op
            self.waiting_for_operand = True
    
    def calculate(self):
        """Perform calculation."""
        if self.first_number is not None and self.operation and self.current_input:
            try:
                second_number = float(self.current_input)
                
                if self.operation == '+':
                    result = self.calc.add(self.first_number, second_number)
                elif self.operation == '-':
                    result = self.calc.subtract(self.first_number, second_number)
                elif self.operation == '×':
                    result = self.calc.multiply(self.first_number, second_number)
                elif self.operation == '÷':
                    result = self.calc.divide(self.first_number, second_number)
                
                self.current_input = str(result)
                self.display_var.set(self.current_input)
                self.first_number = None
                self.operation = None
                self.waiting_for_operand = True
                
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                self.clear()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
                self.clear()
    
    def clear(self):
        """Clear the calculator."""
        self.current_input = "0"
        self.display_var.set(self.current_input)
        self.first_number = None
        self.operation = None
        self.waiting_for_operand = False
    
    def square_root(self):
        """Calculate square root."""
        if self.current_input:
            try:
                number = float(self.current_input)
                result = self.calc.square_root(number)
                self.current_input = str(result)
                self.display_var.set(self.current_input)
                self.waiting_for_operand = True
            except ValueError as e:
                messagebox.showerror("Error", str(e))
    
    def square(self):
        """Calculate square."""
        if self.current_input:
            try:
                number = float(self.current_input)
                result = self.calc.power(number, 2)
                self.current_input = str(result)
                self.display_var.set(self.current_input)
                self.waiting_for_operand = True
            except ValueError as e:
                messagebox.showerror("Error", str(e))
    
    def factorial(self):
        """Calculate factorial."""
        if self.current_input:
            try:
                number = int(float(self.current_input))
                result = self.calc.factorial(number)
                self.current_input = str(result)
                self.display_var.set(self.current_input)
                self.waiting_for_operand = True
            except ValueError as e:
                messagebox.showerror("Error", str(e))
    
    def negate(self):
        """Negate the current number."""
        if self.current_input and self.current_input != "0":
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.display_var.set(self.current_input)
    
    def memory_store(self):
        """Store current value in memory."""
        if self.current_input:
            try:
                value = float(self.current_input)
                self.calc.memory_store(value)
                messagebox.showinfo("Memory", f"Value {value} stored in memory")
            except ValueError:
                messagebox.showerror("Error", "Invalid number")
    
    def memory_recall(self):
        """Recall value from memory."""
        value = self.calc.memory_recall()
        self.current_input = str(value)
        self.display_var.set(self.current_input)
        self.waiting_for_operand = True
    
    def memory_clear(self):
        """Clear memory."""
        self.calc.memory_clear()
        messagebox.showinfo("Memory", "Memory cleared")
    
    def show_history(self):
        """Show calculation history."""
        history = self.calc.get_history()
        if history:
            history_window = tk.Toplevel(self.root)
            history_window.title("Calculation History")
            history_window.geometry("400x300")
            
            # Create scrollable text widget
            frame = ttk.Frame(history_window, padding="10")
            frame.pack(fill=tk.BOTH, expand=True)
            
            text_widget = tk.Text(frame, wrap=tk.WORD, font=("Courier", 10))
            scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text_widget.yview)
            text_widget.configure(yscrollcommand=scrollbar.set)
            
            text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Add history to text widget
            for i, operation in enumerate(history, 1):
                text_widget.insert(tk.END, f"{i:3d}. {operation}\n")
            
            text_widget.config(state=tk.DISABLED)
            
            # Clear history button
            ttk.Button(history_window, text="Clear History", 
                      command=lambda: self.clear_history_and_close(history_window)).pack(pady=5)
        else:
            messagebox.showinfo("History", "No calculations in history yet.")
    
    def clear_history_and_close(self, window):
        """Clear history and close history window."""
        self.calc.clear_history()
        window.destroy()
        messagebox.showinfo("History", "History cleared")


def main():
    """Main function to run the GUI calculator."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()


if __name__ == "__main__":
    main()
