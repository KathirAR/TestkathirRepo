# Addition Program 🧮

A comprehensive Python program that demonstrates various addition operations.

**Author:** Kathir (via Codegen)  
**Created for:** ClickUp task "Addition" program

## Features

- ✅ Add two numbers
- ✅ Add multiple numbers
- ✅ Interactive mode for user input
- ✅ Demo mode with examples
- ✅ Support for integers and decimals
- ✅ Support for negative numbers
- ✅ Error handling for invalid inputs

## How to Run

### Prerequisites
- Python 3.x installed on your system

### Running the Program

```bash
python3 addition_program.py
```

### Program Options

When you run the program, you'll see three options:

1. **Interactive Addition**: Enter your own numbers to add
2. **Demo Mode**: See pre-configured examples
3. **Exit**: Quit the program

## Examples

### Demo Output
```
🔢 Addition Program Demo 🔢
==============================
Demo 1: 5 + 3 = 8
Demo 2: 2.5 + 3.7 = 6.2
Demo 3: 1 + 2 + 3 + 4 + 5 = 15
Demo 4: -10 + 15 = 5
==============================
```

### Interactive Mode
```
🧮 Welcome to the Addition Program! 🧮
========================================
How many numbers would you like to add? 3
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30

========================================
Numbers entered: 10.0, 20.0, 30.0
Sum: 60.0
========================================
```

## Functions

### `add_two_numbers(a, b)`
Adds two numbers and returns the result.

### `add_multiple_numbers(*numbers)`
Adds any number of arguments and returns the sum.

### `interactive_addition()`
Provides an interactive interface for user input.

### `demo_addition()`
Demonstrates various addition scenarios.

## Error Handling

The program includes robust error handling for:
- Invalid numeric input
- Non-numeric input
- Keyboard interrupts (Ctrl+C)
- Edge cases (negative numbers, decimals)

## Testing

You can test the program by running it and trying different scenarios:
- Positive numbers
- Negative numbers  
- Decimal numbers
- Large numbers
- Invalid inputs (to test error handling)

---

*This addition program was created as part of the ClickUp task management system.*
