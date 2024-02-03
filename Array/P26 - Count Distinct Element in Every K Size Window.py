# Time Complexity: O(N * k) where N is the length of the array and k is the window size
# Space Complexity: O(1)

# ALGO:
# 1. Iterate through the array from index 0 to len(arr)-k.
# 2. For each iteration, create a window of size k starting from the current index.
# 3. Count the distinct elements in the window using a set and append the count to the result list.
# 4. Return the list containing counts of distinct elements in each window.

def countDistinctElements(arr, k):
    distinctElements = []  # Initialize an empty list to store counts of distinct elements
    for i in range(len(arr)-k+1):  # Iterate through the array from index 0 to len(arr)-k
        distinctElements.append(len(set(arr[i:i+k])))  # Count distinct elements in the window of size k and append to the result list
    return distinctElements  # Return the list containing counts of distinct elements in each window

# Example usage:
arr = [1, 2, 1, 3, 4, 2, 3]
k = 3
print(countDistinctElements(arr, k))  # Output: [2, 3, 3, 3, 2] for windows [1, 2, 1], [2, 1, 3], [1, 3, 4], [3, 4, 2], [4, 2, 3]
