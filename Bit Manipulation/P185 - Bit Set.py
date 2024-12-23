# Time Complexity: O(n), where n is the length of the input string `digitPattern`.
# - Each digit is processed once, resulting in a linear traversal of the input.

# Space Complexity: O(1).
# - A single integer `seen` is used to track the bits corresponding to digits, requiring constant space.

# INTUITION:
# The goal is to find the first repeating digit in a string of digits. A simple but efficient way to achieve this
# is by using bitwise operations to track the presence of each digit. 
# Each digit is represented as a bit in an integer, allowing us to efficiently check for duplicates.

# ALGO:
# 1. Initialize an integer `seen` to 0. This will act as a bitmask to track digits that have been encountered.
# 2. Iterate through the string `digitPattern`:
#    - For each digit, calculate its corresponding bit position using `1 << int(digit)`.
#    - Check if the bit is already set in `seen` using a bitwise AND operation.
#    - If the bit is set, return the digit as the first repeating digit.
#    - Otherwise, set the bit in `seen` using a bitwise OR operation.
# 3. If no digit repeats, return -1.

from sys import *
from collections import *
from math import *

def findFirstRepeatingDigit(digitPattern):
    seen = 0  # Bitmask to track digits
    for digit in digitPattern:  # Iterate through each character in the string
        bit = 1 << int(digit)  # Calculate the bit position for the current digit
        if seen & bit:  # Check if the bit is already set
            return int(digit)  # Return the first repeating digit

        seen |= bit  # Mark the current digit as seen

    return -1  # If no repeating digit is found, return -1
