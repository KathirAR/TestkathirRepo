#!/usr/bin/env python3
"""
Palindrome Checker and Generator

This module provides various functions to work with palindromes:
- Check if a string is a palindrome
- Find the longest palindromic substring
- Generate palindromes
- Check numeric palindromes

Author: Kathir (via Codegen)
"""

import re
from typing import List, Optional


def is_palindrome(text: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
    """
    Check if a string is a palindrome.
    
    Args:
        text: The string to check
        ignore_case: Whether to ignore case differences
        ignore_spaces: Whether to ignore spaces and punctuation
    
    Returns:
        True if the string is a palindrome, False otherwise
    
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    if not text:
        return True
    
    # Clean the text if needed
    if ignore_spaces:
        # Keep only alphanumeric characters
        text = re.sub(r'[^a-zA-Z0-9]', '', text)
    
    if ignore_case:
        text = text.lower()
    
    # Check if text equals its reverse
    return text == text[::-1]


def is_numeric_palindrome(number: int) -> bool:
    """
    Check if a number is a palindrome.
    
    Args:
        number: The number to check
    
    Returns:
        True if the number is a palindrome, False otherwise
    
    Examples:
        >>> is_numeric_palindrome(121)
        True
        >>> is_numeric_palindrome(12321)
        True
        >>> is_numeric_palindrome(123)
        False
    """
    return str(number) == str(number)[::-1]


def longest_palindromic_substring(text: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    Args:
        text: The input string
    
    Returns:
        The longest palindromic substring
    
    Examples:
        >>> longest_palindromic_substring("babad")
        'bab'
        >>> longest_palindromic_substring("cbbd")
        'bb'
    """
    if not text:
        return ""
    
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(text) and text[left] == text[right]:
            left -= 1
            right += 1
        return text[left + 1:right]
    
    longest = ""
    
    for i in range(len(text)):
        # Check for odd-length palindromes (center is a single character)
        palindrome1 = expand_around_center(i, i)
        # Check for even-length palindromes (center is between two characters)
        palindrome2 = expand_around_center(i, i + 1)
        
        # Update longest if we found a longer palindrome
        for palindrome in [palindrome1, palindrome2]:
            if len(palindrome) > len(longest):
                longest = palindrome
    
    return longest


def generate_palindromes(length: int) -> List[str]:
    """
    Generate all possible palindromes of a given length using lowercase letters.
    
    Args:
        length: The desired length of palindromes
    
    Returns:
        List of all possible palindromes of the given length
    
    Note:
        This function is practical only for small lengths due to exponential growth.
    """
    if length <= 0:
        return []
    
    if length == 1:
        return [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
    palindromes = []
    half_length = (length + 1) // 2
    
    def generate_half(current: str, remaining: int):
        if remaining == 0:
            # Create palindrome by mirroring the half
            if length % 2 == 0:
                palindrome = current + current[::-1]
            else:
                palindrome = current + current[-2::-1]
            palindromes.append(palindrome)
            return
        
        for char in 'abcdefghijklmnopqrstuvwxyz':
            generate_half(current + char, remaining - 1)
    
    generate_half("", half_length)
    return palindromes


def find_palindromes_in_text(text: str, min_length: int = 3) -> List[str]:
    """
    Find all palindromes in a given text.
    
    Args:
        text: The input text to search
        min_length: Minimum length of palindromes to find
    
    Returns:
        List of unique palindromes found in the text
    
    Examples:
        >>> find_palindromes_in_text("The racecar was fast, madam!")
        ['racecar', 'madam']
    """
    # Clean text and convert to lowercase
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    words = clean_text.split()
    
    palindromes = set()
    
    # Check individual words
    for word in words:
        if len(word) >= min_length and is_palindrome(word):
            palindromes.add(word)
    
    # Check substrings
    for i in range(len(clean_text)):
        for j in range(i + min_length, len(clean_text) + 1):
            substring = clean_text[i:j].replace(' ', '')
            if len(substring) >= min_length and is_palindrome(substring):
                palindromes.add(substring)
    
    return sorted(list(palindromes))


def main():
    """
    Demonstrate palindrome functionality with examples.
    """
    print("🔄 Palindrome Checker and Generator 🔄")
    print("=" * 40)
    
    # Test string palindromes
    test_strings = [
        "racecar",
        "A man a plan a canal Panama",
        "race a car",
        "hello world",
        "Madam",
        "Was it a car or a cat I saw?",
        ""
    ]
    
    print("\n📝 String Palindrome Tests:")
    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")
    
    # Test numeric palindromes
    test_numbers = [121, 12321, 123, 1, 1001, 12345]
    
    print("\n🔢 Numeric Palindrome Tests:")
    for num in test_numbers:
        result = is_numeric_palindrome(num)
        print(f"{num} -> {result}")
    
    # Find longest palindromic substring
    test_text = "babad"
    longest = longest_palindromic_substring(test_text)
    print(f"\n🔍 Longest palindrome in '{test_text}': '{longest}'")
    
    # Find palindromes in text
    sample_text = "The racecar was fast, and madam was driving it. Did you see that civic?"
    found_palindromes = find_palindromes_in_text(sample_text)
    print(f"\n🎯 Palindromes found in text: {found_palindromes}")
    
    # Generate small palindromes (only for length 2 to avoid too many results)
    print(f"\n🎲 Sample 2-letter palindromes: {generate_palindromes(2)[:10]}...")
    
    print("\n✨ Palindrome demonstration complete!")


if __name__ == "__main__":
    main()
