# Time Complexity: O(m + n)
# Space Complexity: O(m + n)

# INTUITION:
# To find the median of two sorted arrays, we need to merge them into a single sorted array and then find the median of the resulting array. The merged array will have a length equal to the sum of the lengths of the two input arrays. The median can then be found based on whether the merged array has an odd or even number of elements.

# ALGO:
# 1. Initialize two indices, `index1` and `index2`, to traverse through `nums1` and `nums2` respectively.
# 2. Create an empty list `temp` to store the merged elements.
# 3. Traverse both arrays and compare the current elements:
#    - Append the smaller element to `temp` and move the corresponding index.
# 4. If there are remaining elements in `nums1`, append them to `temp`.
# 5. If there are remaining elements in `nums2`, append them to `temp`.
# 6. Calculate the middle index `mid` of the merged array `temp`.


def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    index1, index2 = 0, 0
    temp = []
    
    while index1 < n and index2 < m:
        if arr1[index1] < arr2[index2]:
            temp.append(arr1[index1])
            index1 += 1
        else:
            temp.append(arr2[index2])
            index2 += 1

    if index1 < n:
        temp.extend(arr1[index1:])

    if index2 < m:
        temp.extend(arr2[index2:])

    return temp[k-1]
        
