from collections import deque

# Time Complexity: O(n)
# Each element is processed at most twice (added and removed once from the deque), so the time complexity is linear with respect to the number of elements in `arr`.

# Space Complexity: O(k)
# The deque will store at most `k` indices at any given time, where `k` is the window size.

# Intuition:
# To find the maximum in each sliding window efficiently, we use a deque to keep track of indices in a way that maintains the maximum of each window at the front.
# The deque is maintained in a decreasing order of values. As we slide the window, we remove indices that:
# 1. Are out of the window's current range.
# 2. Are smaller than the current element, as they can no longer be the maximum in future windows.

# Algorithm:
# 1. Initialize a deque and a result list.
# 2. Process the first `k` elements to fill the deque with the initial window's potential maximum.
# 3. For each remaining element in `arr`, append the current maximum to `ans`, update the deque for the new window,
#    and remove elements that are out of range or smaller than the current element.
# 4. Append the maximum of the last window to `ans`.

def slidingWindowMaximum(arr: list, k: int) -> list:
    dq = deque()
    ans = []

    for i in range(k):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)

    for i in range(k, len(arr)):
        ans.append(arr[dq[0]])

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()

        dq.append(i)

    ans.append(arr[dq[0]])
    return ans
