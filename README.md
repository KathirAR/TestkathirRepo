# Add Two Numbers

A simple Python project that demonstrates how to add two numbers together.

## Features

- ✅ Add two integers
- ✅ Add two floating-point numbers  
- ✅ Add mixed integer and float types
- ✅ Handle negative numbers
- ✅ Interactive command-line interface
- ✅ Comprehensive test suite

## Usage

### Running the Program

```bash
python add_numbers.py
```

This will:
1. Show an example of adding 10 + 25
2. Prompt you to enter two numbers for addition

### Using as a Module

```python
from add_numbers import add_two_numbers

result = add_two_numbers(5, 3)
print(result)  # Output: 8
```

### Running Tests

```bash
python test_add_numbers.py
```

Or using unittest:

```bash
python -m unittest test_add_numbers.py
```

## Examples

```python
# Adding integers
add_two_numbers(10, 5)    # Returns: 15

# Adding floats
add_two_numbers(2.5, 1.5) # Returns: 4.0

# Adding negative numbers
add_two_numbers(-3, 7)    # Returns: 4

# Adding mixed types
add_two_numbers(5, 2.5)   # Returns: 7.5
```

## Files

- `add_numbers.py` - Main module with the addition function
- `test_add_numbers.py` - Unit tests for the addition function
- `README.md` - This documentation file

## Requirements

- Python 3.x

No external dependencies required!

