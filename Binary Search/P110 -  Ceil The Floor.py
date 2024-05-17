# Time Complexity: O(log n)
# Space Complexity: O(1)

# INTUITION:
# The goal is to find the floor and ceiling of a given value `x` in a sorted list `nums`.
# The floor of `x` is the largest element in `nums` that is less than or equal to `x`.
# The ceiling of `x` is the smallest element in `nums` that is greater than or equal to `x`.
# Since the list is sorted, we can use binary search to efficiently find the positions where
# `x` would fit, giving us the floor and ceiling in O(log n) time.
# If `x` is smaller than the smallest element, the floor doesn't exist, and if `x` is larger
# than the largest element, the ceiling doesn't exist.

# ALGO:
# 1. INITIALIZE the search boundaries with `l` set to 0 and `r` set to len(nums) - 1.
# 2. CHECK edge cases where `x` is outside the bounds of `nums`.
#     2.1 IF `x` is smaller than the smallest element, return -1 as floor and the smallest element as ceiling.
#     2.2 IF `x` is larger than the largest element, return the largest element as floor and -1 as ceiling.
# 3. USE binary search to find the correct positions for the floor and ceiling.
#     3.1 CALCULATE `mid` as the midpoint between `l` and `r`.
#     3.2 IF `nums[mid]` is greater than `x`, adjust the right boundary `r` to `mid - 1`.
#     3.3 ELSE IF `nums[mid]` is less than `x`, adjust the left boundary `l` to `mid + 1`.
#     3.4 ELSE `nums[mid]` is equal to `x`, return `nums[mid]` for both floor and ceiling.
# 4. AFTER the loop, `r` will be the index of the largest element less than or equal to `x` (floor),
#    and `l` will be the index of the smallest element greater than or equal to `x` (ceiling).
# 5. RETURN `nums[r]` as the floor and `nums[l]` as the ceiling.

# RETURN the calculated floor and ceiling.

def getFloorAndCeil(nums, n, x):
    if x < nums[0]:
        return -1, nums[0]
    if x > nums[-1]:
        return nums[-1], -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r-l) // 2
        if nums[mid] > x:
            r = mid - 1
        elif nums[mid] < x:
            l = mid + 1
        else:
            return nums[mid], nums[mid]
    return nums[r], nums[l]
