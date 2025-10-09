# 🧮 Calculator Program

A comprehensive calculator program with both command-line interface (CLI) and graphical user interface (GUI) implementations.

## Features

### Basic Operations
- ➕ Addition
- ➖ Subtraction  
- ✖️ Multiplication
- ➗ Division
- 🔢 Power/Exponentiation
- √ Square Root

### Scientific Operations
- ❗ Factorial
- 📐 Trigonometric functions (sin, cos, tan) with degree/radian support
- 📊 Logarithmic functions (natural log, base 10 log, custom base)

### Memory Operations
- 💾 Memory Store (MS)
- 🔄 Memory Recall (MR)
- 🗑️ Memory Clear (MC)

### Additional Features
- 📜 Calculation History (up to 100 operations)
- ⚠️ Comprehensive error handling
- 🎯 Input validation
- 🧪 Full test coverage

## Files

- `calculator.py` - Main calculator class and CLI interface
- `calculator_gui.py` - GUI interface using tkinter
- `test_calculator.py` - Comprehensive test suite
- `CALCULATOR_README.md` - This documentation file

## Usage

### Command Line Interface

Run the CLI version:
```bash
python calculator.py
```

The CLI provides a menu-driven interface with options 0-17:

```
🧮 CALCULATOR PROGRAM
==================================================
Basic Operations:
  1. Addition (+)
  2. Subtraction (-)
  3. Multiplication (×)
  4. Division (÷)
  5. Power (^)
  6. Square Root (√)

Scientific Operations:
  7. Factorial (!)
  8. Sine (sin)
  9. Cosine (cos)
 10. Tangent (tan)
 11. Natural Logarithm (ln)
 12. Logarithm base 10 (log₁₀)

Memory Operations:
 13. Store in Memory (MS)
 14. Recall from Memory (MR)
 15. Clear Memory (MC)

Utility:
 16. Show History
 17. Clear History
  0. Exit
```

### Graphical User Interface

Run the GUI version:
```bash
python calculator_gui.py
```

The GUI provides:
- 📱 Calculator-style button layout
- 🖥️ Digital display
- 🔘 Memory function buttons (MC, MR, MS)
- 🧮 Scientific function buttons (√, x², x!, ±)
- 📜 History window with scrollable view
- ⚠️ Error dialogs for invalid operations

### Running Tests

Execute the test suite:
```bash
python test_calculator.py
```

Or run with unittest:
```bash
python -m unittest test_calculator.py -v
```

## Examples

### CLI Examples

```bash
# Basic arithmetic
Enter your choice (0-17): 1
Enter first number: 15
Enter second number: 25
✅ Result: 15.0 + 25.0 = 40.0

# Scientific functions
Enter your choice (0-17): 8
Enter angle: 90
Use degrees? (y/n): y
✅ Result: sin(90°) = 1.0

# Memory operations
Enter your choice (0-17): 13
Enter value to store: 42
✅ Value 42.0 stored in memory
```

### Programming Interface

```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(10, 5)        # 15.0
result = calc.multiply(3, 4)    # 12.0
result = calc.divide(20, 4)     # 5.0

# Scientific operations
result = calc.square_root(16)   # 4.0
result = calc.factorial(5)      # 120
result = calc.sin(90, degrees=True)  # 1.0

# Memory operations
calc.memory_store(42)
value = calc.memory_recall()    # 42.0

# History
history = calc.get_history()
calc.clear_history()
```

## Error Handling

The calculator includes comprehensive error handling for:

- ❌ Division by zero
- ❌ Square root of negative numbers
- ❌ Factorial of negative numbers
- ❌ Logarithm of non-positive numbers
- ❌ Invalid input types
- ❌ Overflow conditions

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)
- Standard library modules: `math`, `unittest`, `sys`, `typing`

## Testing

The test suite includes:

- ✅ Unit tests for all calculator operations
- ✅ Edge case testing (large numbers, precision, infinity)
- ✅ Error condition testing
- ✅ Memory operation testing
- ✅ History functionality testing

Test coverage includes over 30 test cases covering normal operations, edge cases, and error conditions.

## Architecture

### Calculator Class
The core `Calculator` class provides:
- All mathematical operations as methods
- History tracking with automatic limit management
- Memory storage functionality
- Comprehensive error handling

### GUI Implementation
- Built with tkinter for cross-platform compatibility
- Responsive button layout
- Real-time display updates
- Modal dialogs for errors and confirmations

### CLI Implementation
- Menu-driven interface
- Input validation and error recovery
- Formatted output with emojis for better UX
- Graceful exit handling

## License

This calculator program is provided as-is for educational and practical use.

---

*Created as part of ClickUp task: Calculator program*
