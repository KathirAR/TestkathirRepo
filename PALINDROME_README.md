# 🔄 Palindrome Implementation

A comprehensive palindrome checker and generator implemented in Python.

## Features

### ✅ String Palindrome Checking
- Case-insensitive checking
- Ignores spaces and punctuation
- Handles empty strings and single characters

### 🔢 Numeric Palindrome Checking
- Checks if numbers read the same forwards and backwards
- Works with any integer

### 🔍 Longest Palindromic Substring
- Finds the longest palindromic substring in any given text
- Uses efficient expand-around-center algorithm

### 🎲 Palindrome Generation
- Generates all possible palindromes of a given length
- Uses lowercase letters a-z

### 🎯 Text Analysis
- Finds all palindromes within a given text
- Configurable minimum length
- Returns unique palindromes sorted alphabetically

## Usage

### Basic Usage

```python
from palindrome import is_palindrome, is_numeric_palindrome

# Check string palindromes
print(is_palindrome("racecar"))  # True
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))  # False

# Check numeric palindromes
print(is_numeric_palindrome(121))  # True
print(is_numeric_palindrome(123))  # False
```

### Advanced Features

```python
from palindrome import longest_palindromic_substring, find_palindromes_in_text

# Find longest palindrome in text
longest = longest_palindromic_substring("babad")
print(longest)  # "bab"

# Find all palindromes in text
text = "The racecar was fast, madam!"
palindromes = find_palindromes_in_text(text)
print(palindromes)  # ['madam', 'racecar']
```

### Running the Demo

```bash
python palindrome.py
```

This will run a comprehensive demonstration showing:
- String palindrome tests
- Numeric palindrome tests
- Longest palindromic substring finding
- Palindrome detection in text
- Sample palindrome generation

### Running Tests

```bash
python test_palindrome.py
```

This will run the complete test suite to verify all functionality works correctly.

## Examples

### String Palindromes
- ✅ "racecar" → True
- ✅ "A man a plan a canal Panama" → True
- ✅ "Madam" → True
- ❌ "hello" → False

### Numeric Palindromes
- ✅ 121 → True
- ✅ 12321 → True
- ❌ 123 → False

### Complex Text Analysis
Input: "The racecar was fast, and madam was driving it."
Found palindromes: ['madam', 'racecar']

## Algorithm Details

### Palindrome Checking
- **Time Complexity**: O(n) where n is the length of the string
- **Space Complexity**: O(1) for basic checking, O(n) when cleaning text

### Longest Palindromic Substring
- **Algorithm**: Expand around center
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)

### Palindrome Generation
- **Time Complexity**: O(26^(n/2)) where n is the desired length
- **Space Complexity**: O(26^(n/2))
- **Note**: Practical only for small lengths due to exponential growth

## Author

**Kathir** (via Codegen)  
*Created for ClickUp task: "Palindrome"*

---

*This implementation provides a robust and efficient solution for all palindrome-related operations.*
