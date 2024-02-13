
def sumOfAllDivisors(n: int) -> int:
    ans = n
    for i in range(2,n+1):
       ans += i*(n//i)
    return ans




