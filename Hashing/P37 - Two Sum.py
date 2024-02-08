# Time Complexity: O(n), where n is the length of the input array 'arr'.
# Space Complexity: O(n), where n is the length of the input array 'arr'.

# INTUITION:
# The function 'twoSum' aims to find pairs of elements in the input array 'arr' such that they add up to the target value.
# It uses a defaultdict to keep track of the occurrences of elements in the input array 'arr'.
# The function iterates through each element in the array 'arr' and calculates the complement needed to reach the target value.
# If the complement is seen before, the function appends the pair (arr[i], complement) to the answer list 'ans' and decrements the count of the complement in the defaultdict 'seen'.
# Otherwise, it increments the count of the current element in the defaultdict 'seen'.
# Finally, it returns the answer list 'ans' if it is not empty, otherwise, it returns a default value [(-1, -1)].

# ALGORITHM:
# 1. Initialize a defaultdict 'seen' to keep track of the occurrences of elements in the input array 'arr'.
# 2. Initialize an empty list 'ans' to store pairs of elements that add up to the target value.
# 3. Iterate through each element 'arr[i]' in the input array 'arr':
#       - Calculate the complement 'compliment' needed to reach the target value.
#       - If the count of 'compliment' in the defaultdict 'seen' is not zero:
#               - Append the pair (arr[i], complement) to the answer list 'ans'.
#               - Decrement the count of 'compliment' in the defaultdict 'seen'.
#       - Otherwise, increment the count of 'arr[i]' in the defaultdict 'seen'.
# 4. Return the answer list 'ans' if it is not empty, otherwise, return a default value [(-1, -1)].

from collections import defaultdict

def twoSum(arr, target, n):
    seen = defaultdict(int)  # Initialize defaultdict to store occurrences of elements
    ans = []  # Initialize list to store pairs of elements that add up to target
    for i in range(n):
        complement = target - arr[i]  # Calculate complement needed to reach target
        if seen[complement] != 0:  # If complement is in seen dictionary and its count is not zero
            ans.append((arr[i], complement))  # Add pair (arr[i], complement) to answer list
            seen[complement] -= 1  # Decrement count of complement in seen dictionary
        else:
            seen[arr[i]] += 1  # Increment count of arr[i] in seen dictionary
    return ans if ans else [(-1, -1)]  # Return answer list or default value if no pairs found

# Example usage:
arr = [1, 0, 0, 1, 1]
target = 2
n = len(arr)
print(twoSum(arr, target, n))  # Output: [(0, 2)]
