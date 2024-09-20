# Time Complexity: O(n), where n is the number of elements in the array `arr`. We iterate through the array once and perform constant-time operations with the hash map.
# Space Complexity: O(n), since we use a hash map to store the frequency of the XOR values.

# INTUITION:
# The problem is to find the number of subarrays whose XOR is equal to a given value `x`. 
# We use the XOR prefix sum technique. If the XOR of elements from the start to index `i` is `xor` and XOR from the start to some earlier index `j-1` is `t`, then XOR of elements between index `j` and `i` is `x` if `t ^ xor == x`.

# ALGO:
# 1. Initialize `cnt` to count the number of subarrays and `xor` to keep the cumulative XOR of elements in the array.
# 2. Use a hash map `hash` to store the frequency of each XOR value encountered, with `hash[0] = 1` to handle subarrays starting from index 0.
# 3. Iterate through the array:
#    - Compute the current XOR value of the subarray ending at the current index.
#    - Calculate `t = xor ^ x`, which is the XOR value we are looking for in the hash map.
#    - If `t` exists in the hash map, add its frequency to the count of subarrays.
#    - Update the hash map with the current XOR value.
# 4. After the loop, return `cnt`, which contains the total number of subarrays whose XOR is equal to `x`.

def subarraysXor(arr, x):
    # Step 1: Initialize variables
    cnt, xor = 0, 0
    hash = {0: 1}  # Initialize the hash map with XOR 0 at count 1 to handle subarrays starting from index 0

    # Step 2: Iterate through the array
    for i in range(len(arr)):
        xor = xor ^ arr[i]  # Update the cumulative XOR

        # Step 3: Calculate the XOR we are looking for
        t = xor ^ x

        # Step 4: If the XOR we are looking for exists, add its count to cnt
        cnt += hash.get(t, 0)

        # Step 5: Update the hash map with the current XOR value
        hash[xor] = hash.get(xor, 0) + 1

    return cnt  # Step 6: Return the total number of subarrays whose XOR is equal to x
