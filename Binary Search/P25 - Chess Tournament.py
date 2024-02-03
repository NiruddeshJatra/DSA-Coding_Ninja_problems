# Time Complexity: O(N * log(N))
# Space Complexity: O(1)

# ALGO:
# 1. Sort the array of room positions.
# 2. Define a binary search function to find the maximum possible minimum distance between rooms.
#     2.1 Initialize low as 0 and high as the maximum possible distance between the first and last rooms.
#     2.2 While low is less than or equal to high:
#         2.2.1 Calculate mid as the average of low and high.
#         2.2.2 Check if it's possible to achieve the desired minimum focus level with mid.
#               - If possible, update result with mid and adjust low to mid + 1.
#               - Otherwise, adjust high to mid - 1.
#     2.3 Return the result obtained.
# 3. Define a function isValid to check if it's possible to achieve a minimum focus level by assigning rooms with minimum distance mid.
#     3.1 Simulate the assignment process and count how many players can be assigned rooms while maintaining this minimum distance.
#     3.2 Return True if it's possible to achieve the desired minimum focus level, otherwise return False.
# 4. Call the binary search function with the sorted array of room positions and return the result.


def isValid(positions, n, c, mid):
    prevRoom = positions[0]
    playersAssigned = 1
    for i in range(1,n):
        if positions[i] - prevRoom >= mid:
            prevRoom = positions[i]
            playersAssigned += 1
        if playersAssigned == c:
            return True
    return False


def chessTournament(positions, n , c):
    positions.sort()
    low, high = 0, positions[-1] - positions[0]
    result = 1
    while low<=high:
        mid = (low+high)//2
        if isValid(positions, n, c, mid):
            low = mid+1
            result = mid
        else:
            high = mid-1
    return result
