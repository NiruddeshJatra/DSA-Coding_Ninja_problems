from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    counts = [0] * (n + 1)
    for edge in edges:
        if edge > n:
            continue;
        counts[edge] += 1
    return counts[1:]
    
    
