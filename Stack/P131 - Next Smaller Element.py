"""
### Problem
Given an array of integers `arr` of size `n`, the task is to find the next smaller element for each element in the array. The next smaller element for an element `x` is the first smaller element on the right side of `x` in the array. If no such element exists, the result should be `-1` for that element.

### Intuition
To find the next smaller element efficiently, we can use a stack to keep track of the elements in a way that helps us quickly find the next smaller element for each item in the array. By iterating from the end of the array to the beginning, we can maintain a stack that helps us determine the next smaller element in constant time for each element.

### Approach
1. **Initialize Variables**: 
   - `stack`: A stack to keep track of elements for which we need to find the next smaller element.
   - `ans`: An array to store the next smaller elements, initialized to `-1` for each position.
2. **Iterate Backwards**: Traverse the array from the end to the beginning:
   - For each element, pop elements from the stack that are greater than or equal to the current element. This ensures that the top of the stack is the next smaller element.
   - If the stack is not empty, the top element of the stack is the next smaller element for the current element.
   - Push the current element onto the stack.
3. **Return Result**: The array `ans` now contains the next smaller elements for each position in the input array.

### Time Complexity
The time complexity is O(n) where n is the number of elements in the array. Each element is pushed and popped from the stack at most once.

### Space Complexity
The space complexity is O(n) for the stack and the result array.

### Code
"""

from typing import List

def nextSmallerElement(arr: List[int], n: int) -> List[int]:
    stack = []  # Stack to keep track of elements
    ans = [-1] * n  # Result array initialized to -1 for each element
    
    # Iterate through the array from the end to the beginning
    for i in range(n-1, -1, -1):
        # Maintain the stack such that the top is the next smaller element
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        
        # If stack is not empty, the top is the next smaller element
        if stack:
            ans[i] = stack[-1]
        
        # Push the current element onto the stack
        stack.append(arr[i])
    
    return ans
