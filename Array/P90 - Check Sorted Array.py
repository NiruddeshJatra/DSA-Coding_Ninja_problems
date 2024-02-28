def isSorted(n: int,  a: [int]) -> int:
    for i in range(1,len(a)):
        if a[i]<a[i-1]:
            return 0
    return 
