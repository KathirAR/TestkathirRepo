# 🧮 Calculator Program

A comprehensive calculator program with both command-line and graphical interfaces, featuring basic arithmetic operations, scientific functions, and calculation history tracking.

**Created for ClickUp task #86d0jt9dz**

## ✨ Features

### Basic Operations
- ➕ Addition
- ➖ Subtraction  
- ✖️ Multiplication
- ➗ Division
- 🔢 Power/Exponentiation
- √ Square Root
- ❗ Factorial

### Scientific Functions
- 📐 Trigonometric functions (sin, cos, tan) with degree/radian support
- 📊 Logarithms (natural and custom base)
- 📈 Percentage calculations
- 🧮 Expression evaluator with support for complex mathematical expressions

### Advanced Features
- 📝 **Calculation History**: Track all your calculations
- 🖥️ **Dual Interface**: Both command-line and GUI versions
- 🛡️ **Error Handling**: Robust error handling for invalid operations
- 🧪 **Comprehensive Testing**: Full test suite included
- 🎯 **Type Safety**: Type hints for better code quality

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- tkinter (usually included with Python)

### Installation
1. Clone or download the calculator files
2. Ensure all files are in the same directory:
   - `calculator.py` - Core calculator engine
   - `calculator_gui.py` - GUI interface
   - `test_calculator.py` - Test suite
   - `CALCULATOR_README.md` - This documentation

## 📖 Usage

### Command-Line Interface
Run the main calculator program:
```bash
python calculator.py
```

This will launch an interactive menu with the following options:
1. Basic arithmetic operations (+, -, ×, ÷)
2. Advanced operations (power, square root, factorial)
3. Scientific functions (sin, cos, tan, log)
4. Percentage calculations
5. Expression evaluator
6. History management

### Graphical User Interface
Run the GUI version:
```bash
python calculator_gui.py
```

The GUI features:
- 🖱️ Click-based number and operation input
- 📱 Calculator-style button layout
- 📊 Real-time history display
- 🔬 Scientific function buttons
- 📋 Full history viewer with clear option

### Running Tests
Execute the test suite to verify functionality:
```bash
python test_calculator.py
```

This will run:
- ✅ Unit tests for all calculator functions
- 🚀 Performance benchmarks
- 🧪 Edge case testing

## 🎯 Examples

### Basic Calculations
```python
from calculator import Calculator

calc = Calculator()

# Basic arithmetic
result = calc.add(10, 5)        # 15.0
result = calc.multiply(3, 4)    # 12.0
result = calc.divide(20, 4)     # 5.0

# Scientific functions
result = calc.square_root(16)   # 4.0
result = calc.sin(90, degrees=True)  # 1.0
result = calc.factorial(5)      # 120
```

### Expression Evaluation
```python
# Complex expressions
result = calc.evaluate_expression("(2 + 3) * 4")  # 20
result = calc.evaluate_expression("sqrt(16) + sin(0)")  # 4.0
result = calc.evaluate_expression("log(e)")  # 1.0
```

### History Management
```python
# View calculation history
history = calc.get_history()
for calculation in history:
    print(calculation)

# Clear history
calc.clear_history()
```

## 🏗️ Architecture

### Core Components

#### `Calculator` Class
The main calculator engine with methods for:
- Arithmetic operations with history tracking
- Scientific functions with error handling
- Expression evaluation with security measures
- History management

#### `CalculatorGUI` Class
Tkinter-based graphical interface featuring:
- Responsive button layout
- Real-time display updates
- History integration
- Error message dialogs

#### Test Suite
Comprehensive testing including:
- Unit tests for all functions
- Edge case validation
- Performance benchmarking
- Error condition testing

## 🛡️ Security Features

- **Safe Expression Evaluation**: Only allows mathematical functions and operators
- **Input Validation**: Prevents invalid operations (division by zero, negative square roots, etc.)
- **Error Handling**: Graceful handling of all error conditions
- **Type Safety**: Proper type checking and conversion

## 🎨 User Experience

### Command-Line Interface
- 🎯 Clear, numbered menu system
- ✅ Visual feedback with emojis
- 🔄 Continuous operation until user exits
- 📝 Input validation with helpful error messages

### Graphical Interface
- 🖱️ Intuitive calculator layout
- 📱 Responsive button design
- 📊 Live history display
- 🪟 Popup windows for detailed history
- 🎨 Modern styling with ttk themes

## 🧪 Testing

The test suite covers:
- ✅ All basic arithmetic operations
- ✅ Scientific function accuracy
- ✅ Error condition handling
- ✅ History functionality
- ✅ Expression evaluation
- ✅ Edge cases and boundary conditions
- ✅ Performance benchmarking

Run tests with: `python test_calculator.py`

## 📊 Performance

- ⚡ Fast calculation processing
- 💾 Efficient memory usage
- 📈 Scalable history storage
- 🔄 Responsive GUI updates

Benchmark results (typical):
- 3000 calculations in ~0.01 seconds
- Average: ~0.003ms per calculation

## 🤝 Contributing

This calculator was created for ClickUp task #86d0jt9dz. The code is well-documented and follows Python best practices:

- 📝 Comprehensive docstrings
- 🏷️ Type hints throughout
- 🧪 Full test coverage
- 🎯 Clear separation of concerns
- 🛡️ Robust error handling

## 📄 License

Created by Codegen for educational and practical use.

## 🎉 Enjoy Calculating!

Whether you need quick arithmetic or complex scientific calculations, this calculator has you covered with both command-line efficiency and GUI convenience! 🚀
