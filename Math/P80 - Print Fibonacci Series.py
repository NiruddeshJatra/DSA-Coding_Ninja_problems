from typing import List

def generateFibonacciNumbers(n: int) -> List[int]:
    dp = [0,1]
    
    if n == 1:
        return [0]
    if n==2:
        return [0,1]
    
    for i in range(2,n):
        dp.append(dp[i-1]+dp[i-2])
        
    return dp

   
