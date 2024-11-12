# Time Complexity: O(log n), where n is the length of the array.
# We use binary search, which divides the search space in half at each step.

# Space Complexity: O(1), as we only use a constant amount of extra space for pointers and a few variables.

# INTUITION:
# Since the array is sorted and every number except one appears twice, we can leverage binary search to find
# the single element in O(log n) time. In pairs, a unique number will disrupt the sequence, allowing us to use
# the parity of indices to check where this disruption occurs. Observing pairs:
# - For a correct pair: arr[mid] == arr[mid + 1] if mid is even, or arr[mid] == arr[mid - 1] if mid is odd.
# - If this condition doesn’t hold, the single element is within the left or current part of the array.
# This approach reduces search space by half each time.

# ALGO:
# 1. Set pointers `l` (start) and `r` (end) to cover the array.
# 2. Use a binary search where mid-point checks are adjusted to maintain even indices for pairing logic.
# 3. Check if mid is the start of a valid pair:
#    - If yes, the unique element must be further right, so adjust `l`.
#    - If no, the unique element is to the left or at mid, so adjust `r`.
# 4. Terminate when l == r, pointing directly to the unique element.
# 5. Return the element at `l`, as it is the single element.

def findUnique(arr):
    l, r = 0, len(arr) - 1
    
    while l < r:
        mid = l + (r - l) // 2
        # Ensure mid is even for pairing
        if mid % 2 == 1:
            mid -= 1
        # If arr[mid] is part of a valid pair, move right
        if arr[mid] == arr[mid + 1]:
            l = mid + 2
        else:  # If arr[mid] is not part of a valid pair, move left
            r = mid
    
    # Return the single element
    return arr[l]
