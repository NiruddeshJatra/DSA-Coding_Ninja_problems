# Time Complexity: O(n log (max-min))
# Space Complexity: O(1)

# INTUITION:
# The problem is to place 'k' cows in 'n' stalls such that the minimum distance between any two cows is maximized. To solve this, we use binary search to find the largest minimum distance possible.
# We start by sorting the stalls and using binary search on the distance. For each mid value of distance, we check if it is possible to place all cows with at least 'mid' distance apart using a helper function 'isPossible'.

# ALGO:
# 1. Sort the stalls array.
# 2. Initialize binary search bounds: 
#    - 'l' as 1 (minimum possible distance).
#    - 'r' as the difference between the maximum and minimum stall positions plus one.
# 3. Use binary search to find the maximum minimum distance:
#    3.1 Calculate mid distance.
#    3.2 Check if it is possible to place cows with at least 'mid' distance apart.
#    3.3 If possible, move to the right half to find a larger distance.
#    3.4 If not possible, move to the left half to find a smaller distance.
# 4. Return the largest minimum distance found.

def aggressiveCows(stalls, k):
    def isPossible(dist):
        cntCows, last = 1, stalls[0]
        for i in range(1, len(stalls)):
            if (stalls[i] - last) >= dist:
                cntCows += 1
                last = stalls[i]
            if cntCows == k:
                return True
        return False

    stalls = sorted(stalls)
    l, r = 1, stalls[-1] - stalls[0] + 1
    while l <= r:
        dist = (l + r) // 2
        if isPossible(dist):
            l = dist + 1
        else:
            r = dist - 1
    return r
