from typing import *
import math

def areaSwitchCase(ch: int, a: List[float]):
    if ch == 1:
        ans = math.pi*(a[0]**2)
        return f"{ans:.5f}"
        
    else:
        ans = a[0]*a[1]
        return f"{ans:.5f}"
