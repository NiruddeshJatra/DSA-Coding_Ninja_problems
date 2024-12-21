# Function to toggle the first k bits of an integer n
# Time Complexity: O(k), where k is the number of bits to toggle
# Space Complexity: O(1), as no extra space is used

def toggleKBits(n, k):
    for i in range(k):
        # Toggle the i-th bit by using XOR with (1 << i)
        n = n ^ (1 << i)

    return n

# Example Usage
# Input: n = 5 (Binary: 101), k = 3
# Output: After toggling the first 3 bits, n = 2 (Binary: 010)
result = toggleKBits(5, 3)
print(result)  # Output: 2
