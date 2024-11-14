# Time Complexity: O(n), where n is the length of the array.
# We iterate over the array once with a sliding window, making this approach linear in time.

# Space Complexity: O(1), as we only store a constant amount of extra information (window sum, min sum, and window pointers).

# INTUITION:
# This problem aims to find the minimum sum of any subarray of size `k` within the array. Using a sliding window approach is ideal because it lets us efficiently calculate the sum of every subarray of length `k` by adjusting the window edges instead of recalculating from scratch. 
# Sliding the window means that each time we move one position forward, we add a new element to the window and remove the first element from the previous window, preserving the total window size at `k`. This approach reduces the time complexity, making it much more efficient than recalculating the sum for each possible subarray.

# ALGO:
# 1. Initialize `ans` as infinity to hold the minimum subarray sum found, `windowSum` as 0 for the current window sum, and `i` as the start pointer of the window.
# 2. Traverse through the array using pointer `j`, representing the end of the current window.
# 3. Add `arr[j]` to `windowSum`, expanding the window to include the current element.
# 4. Once the window size reaches `k` (i.e., `j - i + 1 == k`), check if `windowSum` is less than `ans` and update `ans` if so.
# 5. Then, slide the window by subtracting `arr[i]` from `windowSum` and moving the start pointer `i` forward by one.
# 6. Continue this until all subarrays of length `k` are checked.
# 7. Return `ans`, which now holds the minimum sum of any subarray of length `k`.

def minSubarraySum(arr, n, k):
    ans = float('inf')  # Initialize answer as infinity to find the minimum
    windowSum = 0       # Initialize window sum to 0
    i = 0               # Start of the sliding window

    for j in range(len(arr)):
        # Expand the window by adding the current element
        windowSum += arr[j]

        # When the window reaches the desired size of k
        if (j - i + 1) == k:
            # Update the minimum sum found
            ans = min(ans, windowSum)
            # Slide the window forward: remove the element at `i` from windowSum
            windowSum -= arr[i]
            # Move the start of the window forward
            i += 1

    return ans
