# Time Complexity: O(32 * n), where n is the size of the array.
# - We iterate through all 32 bits (for a 32-bit integer) for each element in the array.
# - This results in a time complexity of O(32 * n), which simplifies to O(n) as 32 is constant.

# Space Complexity: O(1).
# - The algorithm uses a constant amount of space for variables, regardless of the input size.

# INTUITION:
# The problem asks to find the single element in an array where every other element appears exactly three times. 
# A direct approach would involve using a hash map to count occurrences, but this would require O(n) space.
# Instead, we use a bitwise approach to solve the problem with O(1) space.
# The idea is to analyze each bit position (from 0 to 31 for a 32-bit integer) across all numbers in the array.
# For each bit position:
# - Count the number of numbers in the array where the bit is set (1).
# - If the count is not divisible by 3, it means the single element contributes to that bit, so we set that bit in the result.

# ALGO:
# 1. Initialize the result variable `ans` to 0.
# 2. Iterate through all 32 bits (0 to 31) since we are dealing with 32-bit integers.
# 3. For each bit position:
#    a. Count how many numbers in the array have that bit set (1).
#    b. If the count of set bits is not divisible by 3, this bit must belong to the single element, so set the corresponding bit in `ans`.
# 4. Return the final result stored in `ans`.

def elementThatAppearsOnce(arr):
    ans = 0
    for bitIndex in range(32):  # Iterate through all 32 bits
        count = 0
        for num in arr:  # Count numbers with the current bit set
            if num & (1 << bitIndex):
                count += 1

        # If the count is not divisible by 3, set the bit in the result
        if count % 3 == 1:
            ans |= (1 << bitIndex)

    return ans
