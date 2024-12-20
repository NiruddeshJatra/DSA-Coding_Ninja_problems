def doesArrayExist(n: int, x: int) -> int:
    if x < (n*(n+1))//2:
        return 0
    return 1
