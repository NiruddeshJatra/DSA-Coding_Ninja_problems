# Time Complexity: O(1)
# Space Complexity: O(1)

# INTUITION
# As the sum of the array will be larger than the sum of n-1 natural numbers,
# we can subtract to  get the duplicate number


def findDuplicate(arr):
    n = len(arr) - 1
    arrSum = sum(arr)
    expectedSum = (n*(n+1))//2
    return arrSum-expectedSum
