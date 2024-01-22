# Time Complexity: O(nlogn)
# Space Complexity: O(n)


def findSecondLargest(arr):
    sortedArr = sorted(list(set(arr)),reverse=True)
    if len(sortedArr)<=1:
        return -1
    return sortedArr[1]
