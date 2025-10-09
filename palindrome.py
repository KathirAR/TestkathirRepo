#!/usr/bin/env python3
"""
Palindrome Checker Module

This module provides functions to check if strings, numbers, and phrases are palindromes.
A palindrome is a word, phrase, number, or other sequence of characters that reads 
the same forward and backward.

Author: Kathir (via Codegen)
"""

import re
from typing import Union


def is_palindrome_simple(text: str) -> bool:
    """
    Check if a string is a palindrome (case-sensitive, includes spaces and punctuation).
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome_simple("racecar")
        True
        >>> is_palindrome_simple("hello")
        False
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return text == text[::-1]


def is_palindrome(text: str, ignore_case: bool = True, ignore_spaces: bool = True, 
                  ignore_punctuation: bool = True) -> bool:
    """
    Check if a string is a palindrome with various options for normalization.
    
    Args:
        text (str): The string to check
        ignore_case (bool): Whether to ignore case differences
        ignore_spaces (bool): Whether to ignore spaces
        ignore_punctuation (bool): Whether to ignore punctuation
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("Was it a car or a cat I saw?")
        True
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        return True  # Empty string is considered a palindrome
    
    # Normalize the text based on options
    normalized = text
    
    if ignore_case:
        normalized = normalized.lower()
    
    if ignore_spaces:
        normalized = normalized.replace(' ', '')
    
    if ignore_punctuation:
        if ignore_spaces:
            # Remove all non-alphanumeric characters (including spaces)
            normalized = re.sub(r'[^a-zA-Z0-9]', '', normalized)
        else:
            # Remove punctuation but keep spaces
            normalized = re.sub(r'[^a-zA-Z0-9 ]', '', normalized)
    
    return normalized == normalized[::-1]


def is_number_palindrome(number: Union[int, float]) -> bool:
    """
    Check if a number is a palindrome.
    
    Args:
        number (Union[int, float]): The number to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
        
    Examples:
        >>> is_number_palindrome(121)
        True
        >>> is_number_palindrome(123)
        False
        >>> is_number_palindrome(12.21)
        True
    """
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    
    # Convert to string and remove decimal point if it's a whole number
    number_str = str(number)
    if isinstance(number, float) and number.is_integer():
        number_str = str(int(number))
    
    return number_str == number_str[::-1]


def find_palindromes(text: str, min_length: int = 3) -> list:
    """
    Find all palindromic substrings in a given text.
    
    Args:
        text (str): The text to search for palindromes
        min_length (int): Minimum length of palindromes to find
        
    Returns:
        list: List of palindromic substrings found
        
    Examples:
        >>> find_palindromes("abccba")
        ['abccba', 'bccb', 'cc']
        >>> find_palindromes("hello")
        ['ll']
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if min_length < 1:
        raise ValueError("Minimum length must be at least 1")
    
    palindromes = []
    text_lower = text.lower()
    
    # Check all possible substrings
    for i in range(len(text)):
        for j in range(i + min_length, len(text) + 1):
            substring = text_lower[i:j]
            if substring == substring[::-1]:
                palindromes.append(text[i:j])  # Keep original case
    
    # Remove duplicates while preserving order
    seen = set()
    unique_palindromes = []
    for palindrome in palindromes:
        if palindrome.lower() not in seen:
            seen.add(palindrome.lower())
            unique_palindromes.append(palindrome)
    
    return unique_palindromes


def longest_palindrome(text: str) -> str:
    """
    Find the longest palindromic substring in a given text.
    
    Args:
        text (str): The text to search
        
    Returns:
        str: The longest palindromic substring
        
    Examples:
        >>> longest_palindrome("babad")
        'bab'
        >>> longest_palindrome("cbbd")
        'bb'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        return ""
    
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(text) and text[left].lower() == text[right].lower():
            left -= 1
            right += 1
        return text[left + 1:right]
    
    longest = ""
    
    for i in range(len(text)):
        # Check for odd-length palindromes
        palindrome1 = expand_around_center(i, i)
        # Check for even-length palindromes
        palindrome2 = expand_around_center(i, i + 1)
        
        # Update longest if we found a longer palindrome
        for palindrome in [palindrome1, palindrome2]:
            if len(palindrome) > len(longest):
                longest = palindrome
    
    return longest


def main():
    """
    Demonstration of palindrome functions.
    """
    print("🔄 Palindrome Checker Demo 🔄\n")
    
    # Test cases
    test_strings = [
        "racecar",
        "A man a plan a canal Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "Madam",
        "hello world",
        ""
    ]
    
    test_numbers = [121, 123, 12321, 12.21, 123.45]
    
    print("📝 String Palindrome Tests:")
    print("-" * 40)
    for test_str in test_strings:
        result = is_palindrome(test_str)
        print(f"'{test_str}' -> {result}")
    
    print("\n🔢 Number Palindrome Tests:")
    print("-" * 40)
    for test_num in test_numbers:
        result = is_number_palindrome(test_num)
        print(f"{test_num} -> {result}")
    
    print("\n🔍 Finding Palindromes in Text:")
    print("-" * 40)
    sample_text = "abccba racecar hello"
    palindromes = find_palindromes(sample_text)
    print(f"Text: '{sample_text}'")
    print(f"Palindromes found: {palindromes}")
    
    print("\n📏 Longest Palindrome:")
    print("-" * 40)
    sample_text2 = "babad"
    longest = longest_palindrome(sample_text2)
    print(f"Text: '{sample_text2}'")
    print(f"Longest palindrome: '{longest}'")


if __name__ == "__main__":
    main()
