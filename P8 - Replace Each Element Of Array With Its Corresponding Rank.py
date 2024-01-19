# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# ALGO
# 1. SORT the distinct values of arr
# 2. MAP them to a dictionary according to their index+1
# 3. REPLACE values of arr with its rank which is stored in the dictionary. 


from typing import List

def replaceWithRank(arr: List[int],n : int) -> List[int]:
    sortedArr = sorted(set(arr))
    rankDIct = {}
    
    for rank, value in enumerate(sortedArr):
        rankDIct[value] = rank+1

    rankArr = []
    for i in arr:
        rankArr.append(rankDIct[i])

    return rankArr
