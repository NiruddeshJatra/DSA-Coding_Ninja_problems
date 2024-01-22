# Time Complexity: O(nlogn)
# Space Complexity: O(n)

def kthSmallest(arr, k):
    return sorted(arr)[k-1]
