# ------ NAIVE_SOLUTION ------
# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# ALGO
# 1. pairArr = []
# 2. SORT arr
# 3. TRAVERSE arr
# 4. for every i, FIND -i using "binary search"
# 5. IF found, add i and -i to pairArr
# 6. RETURN pairArr

def binarySearch(arr, n):
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] < n:
            l = mid + 1
        elif arr[mid] > n:
            r = mid - 1
        else:
            return True
    return False

def pairs(arr, n):
    arr.sort()
    pairArr = [[]]
    for i in range(n-1):
        if binarySearch(arr[i+1:], -arr[i]):
            pairArr.append([-abs(arr[i]),abs(arr[i])])
    return pairArr




# ------ OPTIMAL_SOLUTION ------
# Time Complexity: O(n)
# Space Complexity: O(n)

# ALGO
# 1. negativeValues = {}, pairArr = [[]]
# 2. TRAVERSE arr
# 3. IF i<0, add i to negativeValues
# 4. TRAVERSE arr
# 5. IF i>0 and -i in negativeValues: add(-i,i) to pairArr
# 6. RETURN pairArr 


def pairs(arr, n):
    negativeValues = {}
    pairArr = [[]]
    
    for i in arr:
        if i<0:
            negativeValues[i] = 1
    
    for i in arr:
        if i>0 and -i in negativeValues:
            pairArr.append([-i,i])
    return pairArr 
