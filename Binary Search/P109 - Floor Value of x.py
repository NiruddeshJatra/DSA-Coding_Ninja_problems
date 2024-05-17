def floorSearch(nums, x, n):
    if x < nums[0]:
        return -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r-l) // 2
        if nums[mid] > x:
            r = mid - 1
        elif nums[mid] < x:
            l = mid + 1
        else:
            return nums[mid]
    return nums[r]
