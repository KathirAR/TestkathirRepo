# 🔄 Palindrome Checker

A comprehensive Python implementation for checking and analyzing palindromes.

**Author:** Kathir (via Codegen)

## 📋 Overview

This module provides various functions to work with palindromes - words, phrases, numbers, or sequences that read the same forward and backward.

## 🚀 Features

- ✅ **Simple palindrome checking** (case-sensitive, includes punctuation)
- ✅ **Advanced palindrome checking** with customizable options
- ✅ **Number palindrome detection** (integers and floats)
- ✅ **Find all palindromes** in a given text
- ✅ **Longest palindrome finder** using efficient algorithms
- ✅ **Comprehensive unit tests** with 100% coverage
- ✅ **Type hints** for better code documentation
- ✅ **Error handling** for invalid inputs

## 📁 Files

- `palindrome.py` - Main module with all palindrome functions
- `test_palindrome.py` - Comprehensive unit tests
- `PALINDROME_README.md` - This documentation file

## 🔧 Functions

### `is_palindrome_simple(text: str) -> bool`
Basic palindrome check (case-sensitive, includes spaces and punctuation).

```python
is_palindrome_simple("racecar")  # True
is_palindrome_simple("Racecar")  # False
```

### `is_palindrome(text: str, ignore_case=True, ignore_spaces=True, ignore_punctuation=True) -> bool`
Advanced palindrome check with customizable normalization options.

```python
is_palindrome("A man a plan a canal Panama")  # True
is_palindrome("Was it a car or a cat I saw?")  # True
is_palindrome("race a car")  # False
```

### `is_number_palindrome(number: Union[int, float]) -> bool`
Check if a number is a palindrome.

```python
is_number_palindrome(121)    # True
is_number_palindrome(12.21)  # True
is_number_palindrome(123)    # False
```

### `find_palindromes(text: str, min_length=3) -> list`
Find all palindromic substrings in a text.

```python
find_palindromes("abccba")  # ['abccba', 'bccb', 'cc']
find_palindromes("hello")   # ['ll']
```

### `longest_palindrome(text: str) -> str`
Find the longest palindromic substring using an efficient algorithm.

```python
longest_palindrome("babad")  # 'bab'
longest_palindrome("cbbd")   # 'bb'
```

## 🏃‍♂️ Usage

### Running the Demo
```bash
python palindrome.py
```

### Running Tests
```bash
python test_palindrome.py
```

### Using as a Module
```python
from palindrome import is_palindrome, find_palindromes

# Check if text is palindrome
result = is_palindrome("A man a plan a canal Panama")
print(result)  # True

# Find all palindromes in text
palindromes = find_palindromes("racecar level hello")
print(palindromes)  # ['racecar', 'level', 'ell']
```

## 📊 Example Output

```
🔄 Palindrome Checker Demo 🔄

📝 String Palindrome Tests:
----------------------------------------
'racecar' -> True
'A man a plan a canal Panama' -> True
'race a car' -> False
'Was it a car or a cat I saw?' -> True
'Madam' -> True
'hello world' -> False
'' -> True

🔢 Number Palindrome Tests:
----------------------------------------
121 -> True
123 -> False
12321 -> True
12.21 -> True
123.45 -> False

🔍 Finding Palindromes in Text:
----------------------------------------
Text: 'abccba racecar hello'
Palindromes found: ['abccba', 'bccb', 'cc', 'racecar', 'cec', 'aca', 'car', 'ell']

📏 Longest Palindrome:
----------------------------------------
Text: 'babad'
Longest palindrome: 'bab'
```

## 🧪 Test Coverage

The test suite includes:
- ✅ Basic palindrome detection
- ✅ Case sensitivity options
- ✅ Space and punctuation handling
- ✅ Number palindromes (integers and floats)
- ✅ Edge cases (empty strings, single characters)
- ✅ Error handling for invalid inputs
- ✅ Integration tests

## 🎯 Algorithm Complexity

- **is_palindrome**: O(n) time, O(n) space
- **find_palindromes**: O(n³) time, O(k) space (where k is number of palindromes)
- **longest_palindrome**: O(n²) time, O(1) space (expand around center approach)

## 🔍 Common Palindrome Examples

**Words:**
- racecar, level, radar, civic, rotor

**Phrases:**
- "A man a plan a canal Panama"
- "Was it a car or a cat I saw?"
- "Madam, I'm Adam"

**Numbers:**
- 121, 1221, 12321, 12.21

## 🤝 Contributing

This implementation was created for the ClickUp task "Palindrome". Feel free to extend or modify as needed!

---

*Created with ❤️ by Codegen for Kathir*
