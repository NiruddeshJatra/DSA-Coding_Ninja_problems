def kJumps(n: int, k: int, a: List[int]) -> int:
    maximumCoinCount = [0]*k
    for i in range(n):
        maximumCoinCount[i%k] += a[i]
    return max(maximumCoinCount)
