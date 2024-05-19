def NthRoot(n: int, m: int) -> int:
    l, r = 1, m
    while l <=r:
        mid = (l+r)//2
        if mid**n > m:
            r = mid - 1
        elif mid**n < m:
            l = mid + 1
        else:
            return mid
            
    return -1
