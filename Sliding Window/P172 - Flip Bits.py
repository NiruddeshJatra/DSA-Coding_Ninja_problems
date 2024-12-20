# Time Complexity: O(n), where n is the size of the input array `arr`.  
# - We traverse the array once, performing constant-time operations for each element.  
# - Hence, the time complexity is linear.

# Space Complexity: O(1).  
# - The solution uses a constant amount of extra space, regardless of the input size.  
# - The variables `countOfOne`, `maxFlipGain`, and `currentGain` are the only additional storage required.

# INTUITION:  
# The task is to maximize the number of 1s in the array by flipping exactly one subarray of 0s to 1s (and vice versa).  
# To achieve this, we first count all the 1s in the array (`countOfOne`).  
# Then, using a variation of Kadane's algorithm, we calculate the maximum "flip gain" by flipping a subarray.  
# - Flipping a 1 decreases the total gain by 1 (because it becomes 0).  
# - Flipping a 0 increases the total gain by 1 (because it becomes 1).  
# We track the maximum `currentGain` and reset it to 0 whenever it becomes negative.  
# Finally, the result is the sum of `countOfOne` and the maximum `maxFlipGain`.

# ALGO:  
# 1. Initialize `countOfOne` to count the total number of 1s in the array.  
# 2. Use a variation of Kadane's algorithm to calculate `maxFlipGain`:  
#    - For each 1, decrease the `currentGain`.  
#    - For each 0, increase the `currentGain`.  
#    - Update `maxFlipGain` as the maximum value of `currentGain`.  
#    - Reset `currentGain` to 0 if it becomes negative.  
# 3. The final answer is `countOfOne + maxFlipGain`.

def flipBits(arr, n): 
    countOfOne = 0  # Count of 1s in the array
    maxFlipGain = 0  # Maximum gain from flipping a subarray
    currentGain = 0  # Current gain from flipping the ongoing subarray

    # Traverse the array
    for num in arr:
        if num == 1:
            countOfOne += 1
            currentGain -= 1  # Flipping a 1 decreases the gain
        else:
            currentGain += 1  # Flipping a 0 increases the gain

        # Update maxFlipGain
        maxFlipGain = max(maxFlipGain, currentGain)

        # Reset currentGain if it becomes negative
        if currentGain < 0:
            currentGain = 0

    # Calculate the final result
    ans = countOfOne + maxFlipGain
    return ans
