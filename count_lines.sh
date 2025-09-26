#!/bin/bash

# Simple bash script to count the number of lines in a file
# Usage: ./count_lines.sh <filename>

# Check if a filename was provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    echo "Example: $0 myfile.txt"
    exit 1
fi

# Store the filename
filename="$1"

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "Error: File '$filename' does not exist."
    exit 1
fi

# Count the lines and display the result
line_count=$(wc -l < "$filename")
echo "Number of lines in '$filename': $line_count"
