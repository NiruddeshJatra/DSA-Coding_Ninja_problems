# Time Complexity: O(logn)
# Space Complexity: O(1)

#ALGO

# CALCULATE common differnece = (arr[n-1] - arr[0])//n
# BINARY SEARCH the arr the find the number that is missing
# RETURN the number

def missingNumber(arr, n):
    commonDiffernece = (arr[n-1] - arr[0])//n
    l, r = 0, n-1
    while l<=r:
        mid = (l+r)//2
        expectedNumber = arr[0] + mid*commonDiffernece
        if arr[mid] == expectedNumber:
            l = mid+1
        else:
            r = mid-1
    return arr[0]+l*commonDiffernece
