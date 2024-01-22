# Time Complexity: O(logn)
# Space Complexity: O(1)

# INTUITION
# use two separate BINARY SEARCH algorithms to find the first occurance of x and the last occurance of x.
# IF found, then (lastOccurance-firstOccurance)+1 will give the total count of x in the arr.

def countOccurrences(arr, x):
    firstOccurance = -1
    l, r = 0, len(arr)-1
    
    while l<=r:
        mid = (l+r)//2
        if arr[mid] >= x:
            r = mid-1
            if arr[mid] == x:
                firstOccurance = mid    
        else:
            l = mid+1
        
    if firstOccurance == -1:
        return 0
    
    lastOccurance = firstOccurance
    l, r = firstOccurance, len(arr)-1

    while l<=r:
        mid = (l+r)//2
        if arr[mid] > x:
            r = mid-1    
        else:
            l = mid+1
            if arr[mid] == x:
                lastOccurance = mid

    return (lastOccurance-firstOccurance)+1
