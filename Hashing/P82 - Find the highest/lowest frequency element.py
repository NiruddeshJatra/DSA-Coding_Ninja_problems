# Time Complexity: O(n)
# Space Complexity: O(n)

# INTUITION:
# This algorithm aims to find the most and least frequent elements in the given list.
# It utilizes a Counter to count the frequencies of each element in the list.

# ALGO:
# 1. Initialize a Counter to count the frequencies of elements in the list.
# 2. Iterate through the items in the Counter.
#    2.1. Update the most frequent element (mx) if the current count is greater or equal to the count of mx.
#    2.2. Update the least frequent element (mn) if the current count is less than or equal to the count of mn.
# 3. Return a list containing the most frequent element (mx) and the least frequent element (mn).

from typing import List
from collections import Counter

def getFrequencies(v: List[int]) -> List[int]:
    # Count the frequencies of elements
    counts = Counter(v)
    
    # Initialize mx and mn with the first element in the list
    mx, mn = v[0], v[0]
    
    # Iterate through the counts
    for num, count in counts.items():
        # Update mx if the current count is greater or equal to the count of mx
        if count >= counts[mx]:
            # If the counts are equal, update mx if the current element is smaller
            if count == counts[mx]:
                if num < mx:
                    mx = num
            else:
                mx = num
        
        # Update mn if the current count is less than or equal to the count of mn
        if count <= counts[mn]:
            # If the counts are equal, update mn if the current element is smaller
            if count == counts[mn]:
                if num < mn:
                    mn = num
            else:
                mn = num
    
    # Return the list containing the most frequent element (mx) and the least frequent element (mn)
    return [mx, mn]
