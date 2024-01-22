# Time Complexity: O(n)
# Space Complexity: O(n)

# ALGO
# 1. CREATE leftProducts and rightProducts array
# 2. INITIALIZE ach element of both arrays to 1
# 3. For each ith element of arr from 1 to n:
#   3.1 CALCULATE the product of all elements to the left
#   3.2 STORE them in leftProducts[i]
# 4. DO the same for the rightProducts
# 5. MULTIPLY the corresponding elements from these two arrays to get the final result
# 6. RETURN result

def productPuzzle(arr):
    n = len(arr)
    leftProducts = [1]*n
    rightProducts = [1]*n

    leftProduct = 1
    for i in range(1,n):
        leftProduct = (leftProduct*arr[i-1])%(10**9+7)
        leftProducts[i] = leftProduct

    rightProduct = 1
    for i in range(n-2,-1,-1):
        rightProduct = (rightProduct*arr[i+1])%(10**9+7)
        rightProducts[i] = rightProduct

    result = [(leftProducts[i]*rightProducts[i])%(10**9+7) for i in range(n)]
    return result
