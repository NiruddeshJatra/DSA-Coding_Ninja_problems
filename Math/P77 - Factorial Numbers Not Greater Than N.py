from typing import *

def factorialNumbers(n: int) -> List[int]:
    ans = []
    factorial, i = 1, 1
    while factorial <= n:
        
        ans.append(factorial)
        i += 1
        factorial *= i
        
    return ans
