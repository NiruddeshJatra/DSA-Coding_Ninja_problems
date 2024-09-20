# Time Complexity: O(n), where n is the number of elements in the array `arr`. We traverse the array once while performing constant-time lookups and updates in the hash map.
# Space Complexity: O(n), since we use a hash map to store the prefix sums and their corresponding indices.

# INTUITION:
# The idea is to use a hash map to store the prefix sum at each index and check if the same sum has appeared before. If it has, that means the subarray between the previous occurrence of that sum and the current index has a sum of 0. We use this property to track the length of the longest such subarray.

# ALGO:
# 1. Initialize `ans` to store the length of the longest subarray and `sum` to store the running sum of the array elements.
# 2. Use a hash map `hash` to store the first occurrence of each prefix sum, with `hash[0] = -1` to handle cases where the subarray starts from index 0.
# 3. Iterate through the array:
#    - Add the current element to `sum`.
#    - If `sum` has been seen before (i.e., it exists in `hash`), calculate the length of the subarray between the previous occurrence and the current index.
#    - If `sum` hasn't been seen before, store the current index in the hash map for that sum.
# 4. After the loop, return `ans`, which contains the length of the longest subarray with a sum of 0.

def lengthOfLongestSubarray(arr, n):
    # Step 1: Initialize variables
    ans, sum = 0, 0
    hash = {0: -1}  # Initialize the hash map with sum 0 at index -1 to handle subarrays starting from index 0

    # Step 2: Iterate through the array
    for i in range(n):
        sum += arr[i]  # Update the running sum
        
        # Step 3: Check if the sum has been seen before
        if sum in hash:
            # Step 4: Calculate the length of the subarray
            ans = max(ans, i - hash[sum])
        else:
            # Step 5: Store the current index in the hash map if the sum is seen for the first time
            hash[sum] = i
            
    return ans  # Step 6: Return the length of the longest subarray
