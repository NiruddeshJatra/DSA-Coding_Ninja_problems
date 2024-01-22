# ------ NAIVE_SOLUTION -----------

# Time_Complexity : o(nlogn)
# Space_Complexity : O(n)

#ALGO
# Sort the array in ascending order
# Retrun the sorted array

def sortBinaryArray(arr, n):
    return sorted(arr)


# -------- OPTIMAL_SOLUTION ----------
# Time_Complexity : o(n)
# Space_Complexity : O(1)

#ALGO
# index = 0
# TRAVERSE the array
# IF i-th element is 0, SWAP(a[i],a[index])
# index++
# RETURN the array

def sortBinaryArray(arr, n):
    index = 0
    for i in range(n):
        if arr[i]==0:
            arr[i],arr[index] = arr[index],arr[i]
            index += 1
    return arr 
