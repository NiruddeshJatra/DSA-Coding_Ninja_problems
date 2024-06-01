# Time Complexity: O(r * log(c) * log(maxVal - minVal))
# Space Complexity: O(1)

# INTUITION:
# The goal is to find the median of a row-wise sorted matrix. 
# We can use a binary search approach to efficiently find the median by leveraging the sorted property of the rows.
# By defining a helper function to find the upper bound of a target value in a row, we can count how many elements in the matrix are less than or equal to a given value.
# Using binary search on the value range of the matrix, we can determine the median by finding the smallest value for which half of the matrix elements are less than or equal to it.

# ALGO:
# 1. Define a helper function `upperBound` that finds the index of the first element greater than a given target in a row using binary search.
# 2. Initialize variables `minVal` and `maxVal` to store the minimum and maximum values in the matrix.
# 3. Iterate through each row to update `minVal` and `maxVal`.
# 4. Use binary search on the range `[minVal, maxVal]` to find the median:
#    a. Calculate `mid` as the middle value of the current range.
#    b. Count the number of elements in the matrix that are less than or equal to `mid` using the `upperBound` function.
#    c. If the count is greater than half the number of elements in the matrix, update `median` and adjust the search range to the left.
#    d. Otherwise, adjust the search range to the right.
# 5. Return the `median` value.

def getMedian(mat):
    def upperBound(arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    median = 10**7
    minVal, maxVal = 10**7, -10**7
    for i in range(len(mat)):
        minVal = min(minVal, mat[i][0])
        maxVal = max(maxVal, mat[i][-1])

    l, r = minVal, maxVal
    while l <= r:
        mid = (l + r) // 2
        cntLowerOrEqualMid = 0
        for row in range(len(mat)):
            cntLowerOrEqualMid += upperBound(mat[row], mid)

        if cntLowerOrEqualMid > (len(mat) * len(mat[0])) // 2:
            median = mid
            r = mid - 1
        else:
            l = mid + 1

    return median
