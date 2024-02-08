# Time Complexity: O(n), where n is the size of the input array 'arr'.
# Space Complexity: O(m), where m is the number of local minima or local maxima in the array.

# INTUITION:
# The function aims to find the indices of local minima and local maxima in the given array 'arr'.
# A local minimum is an element that is smaller than its neighbors, and a local maximum is an element that is larger than its neighbors.

# ALGORITHM:
# 1. Initialize empty lists 'localMin' and 'localMax' to store the indices of local minima and local maxima, respectively.
# 2. Iterate through each element 'arr[i]' in the input array:
#    - Check if 'arr[i]' is a local minimum or local maximum based on its neighbors.
#    - Append the index 'i' to 'localMin' if 'arr[i]' is a local minimum.
#    - Append the index 'i' to 'localMax' if 'arr[i]' is a local maximum.
# 3. If no local maxima or local minima are found, append -1 to the respective list.
# 4. Return a list containing 'localMin' and 'localMax'.

def findLocalMinimaAndMaxima(arr, n):
    localMin = []
    localMax = []
    
    for i in range(n):
        if i == 0:
            if arr[i+1] > arr[i]:
                localMin.append(i)
            elif arr[i+1] < arr[i]:
                localMax.append(i)
        elif i == n-1:
            if arr[i-1] > arr[i]:
                localMin.append(i)
            elif arr[i-1] < arr[i]:
                localMax.append(i)
        else:
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                localMax.append(i)
            if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                localMin.append(i)
    
    if not localMax:
        localMax.append(-1)
    if not localMin:
        localMin.append(-1)
    
    return [localMin, localMax]

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
n = len(arr)
local_minima, local_maxima = findLocalMinimaAndMaxima(arr, n)
print("Local Minima:", local_minima)
print("Local Maxima:", local_maxima)
