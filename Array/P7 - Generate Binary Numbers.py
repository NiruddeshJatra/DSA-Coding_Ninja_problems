# Time Complexity: O(n)
# Space Complexity: O(n)

# ALGO
# python already has a builtin method to convert integer to binary
# Take an array of all numbers from 1 to n, iterate and convert


def generateBinaryNumbers(n):
    binaryNums = []
    for i in range(1,n+1):
        binary = bin(i)[2:]
        binaryNums.append(binary)
    return binaryNums
