# Time Complexity: O(n)
# Space Complexity: O(n)

# ALGO
# 1. COUNT the elements of arr1 and STORE them in a dictionary
# 2. LOOP through arr2
#     - If an element in arr2 is found in the dictionary from step 1:
#         - Decrease its count in the dictionary
#         - If the count becomes negative, return False
#     - If an element in arr2 is not found in the dictionary, return False
# 3. If all elements in arr2 are found in arr1 and their counts are not negative, return True



from collections import Counter

def checkSubset(arr1, arr2, n, m):
    firstArrElementCount = Counter(arr1)
    for i in arr2:
        if i in firstArrElementCount:
            firstArrElementCount[i] -= 1
            if firstArrElementCount[i] < 0:
                return False
        else:
            return False
    return True
