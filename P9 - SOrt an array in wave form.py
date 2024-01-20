# Time Complexity: O(n)
# Space Complexity: O(n)

#ALGO
# 1. TRAVERSE the array
# 2. for the ith index:
#       IF i is odd and arr[i]>arr[i-1]
#            SWAP(arr[i],arr[i-1])
# 3.    ELSE IF arr[i]<arr[i-1]
#            SWAP(arr[i],arr[i-1])
# 4. RETURN arr


def waveFormArray(arr, n):
    for i in range(1,n):
        if i%2==1:
            if arr[i]>arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
        else:
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
    return arr
