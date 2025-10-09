# Addition Program 🧮

**Author:** Kathir (via Codegen)  
**Created for:** ClickUp Task #86d0jt8bn

A comprehensive Python addition program with multiple features and user-friendly interface.

## Features ✨

- **Basic Addition**: Add two numbers together
- **Multiple Number Addition**: Add any number of values
- **Interactive Menu**: User-friendly command-line interface
- **Quick Calculation**: Command-line arguments for fast calculations
- **Input Validation**: Robust error handling for invalid inputs
- **Type Hints**: Full type annotations for better code quality

## Usage 🚀

### Interactive Mode

Run the program without arguments to enter interactive mode:

```bash
python addition_program.py
```

This will display a menu with the following options:
1. Add two numbers
2. Add multiple numbers
3. Quick calculation (command line)
4. Exit

### Quick Calculation Mode

For fast calculations, pass numbers as command-line arguments:

```bash
# Add two numbers
python addition_program.py 5 10

# Add multiple numbers
python addition_program.py 1 2 3 4 5

# Works with decimals and negative numbers
python addition_program.py -5.5 10.2 3.3
```

## Examples 📝

### Interactive Mode Examples

```
🧮 ADDITION PROGRAM
==================================================
1. Add two numbers
2. Add multiple numbers
3. Quick calculation (command line)
4. Exit
==================================================

🔢 Enter your choice (1-4): 1

➕ Adding Two Numbers
-------------------------
Enter first number: 15
Enter second number: 25

✅ Result: 15.0 + 25.0 = 40.0
```

### Command Line Examples

```bash
$ python addition_program.py 10 20
🧮 Quick Calculation:
Numbers: 10.0 + 20.0
Result: 30.0

$ python addition_program.py 1.5 2.5 3.0 4.0
🧮 Quick Calculation:
Numbers: 1.5 + 2.5 + 3.0 + 4.0
Result: 11.0
```

## Testing 🧪

Run the test file to verify all functions work correctly:

```bash
python test_addition.py
```

Expected output:
```
🎯 Running Addition Program Tests
========================================
🧪 Testing add_two_numbers function...
  5 + 3 = 8 (expected 8) ✅ PASS
  10.5 + 2.5 = 13.0 (expected 13.0) ✅ PASS
  -5 + 10 = 5 (expected 5) ✅ PASS
  0 + 0 = 0 (expected 0) ✅ PASS
  -3 + -7 = -10 (expected -10) ✅ PASS

🧪 Testing add_multiple_numbers function...
  [1, 2, 3, 4, 5] = 15 (expected 15) ✅ PASS
  [10.5, 2.5, 7.0] = 20.0 (expected 20.0) ✅ PASS
  [-5, 10, -3] = 2 (expected 2) ✅ PASS
  [0] = 0 (expected 0) ✅ PASS
  [100] = 100 (expected 100) ✅ PASS
  [] = 0 (expected 0) ✅ PASS

🎉 All tests completed!
```

## File Structure 📁

```
├── addition_program.py          # Main program file
├── test_addition.py            # Test file
└── ADDITION_PROGRAM_README.md  # This documentation
```

## Functions 🔧

### `add_two_numbers(a: float, b: float) -> float`
Adds two numbers together.

### `add_multiple_numbers(numbers: List[float]) -> float`
Adds multiple numbers from a list.

### `get_number_input(prompt: str) -> float`
Gets validated number input from user.

### `get_multiple_numbers() -> List[float]`
Gets multiple numbers from user input.

### `display_menu()`
Displays the main program menu.

### `quick_calculation()`
Handles command-line argument calculations.

## Error Handling 🛡️

The program includes comprehensive error handling:
- Invalid number inputs are caught and user is prompted to retry
- Keyboard interrupts (Ctrl+C) are handled gracefully
- Empty input lists are handled appropriately
- Command-line argument validation

## Requirements 📋

- Python 3.6 or higher
- No external dependencies required

## License 📄

Created for educational purposes as part of ClickUp task management.

---

**Happy Adding!** 🎉
