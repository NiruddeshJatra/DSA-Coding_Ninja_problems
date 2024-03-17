# Time Complexity: O(n), where n is the size of the input array `arr`.
# Space Complexity: O(1)

# INTUITION:
# We are traversing the array and keeping track of the number of zeros encountered.
# We adjust the window size (l to r) such that the number of zeros in the window is at most `k`.
# At each step, we update the answer with the maximum length of the valid subsegment.

# ALGO:
# 1. Initialize variables `l` (left pointer), `ans` (answer), and `zeroCount` (count of zeros) to 0.
# 2. Iterate through the array using a sliding window approach:
#    - Increment `zeroCount` when encountering a zero.
#    - Adjust the window by incrementing `l` until the number of zeros in the window is less than or equal to `k`.
#    - Update `ans` with the maximum length of the valid subsegment.
# 3. Return `ans`.

def longestSubSeg(arr, n, k):
    l, ans = 0, 0
    zeroCount = 0
    for r in range(n):
        if arr[r] == 0:
            zeroCount += 1

        while zeroCount > k:
            if arr[l] == 0:
                zeroCount -= 1
            l += 1

        ans = max(ans, r-l+1)

    return ans
