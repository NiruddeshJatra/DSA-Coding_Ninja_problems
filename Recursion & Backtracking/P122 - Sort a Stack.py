"""
### Problem
Given a stack, sort it such that the smallest items are on the top. You can use only an additional stack as a buffer and no other data structures (like arrays or lists).

### Intuition
The problem can be solved using a recursive approach. The idea is to recursively pop elements from the stack and sort the remaining stack. Once the remaining stack is sorted, we insert the popped element back into the sorted stack at its correct position. This ensures the stack is sorted in ascending order from top to bottom.

### Approach
1. Define a helper function `insert` that takes a stack and an element `x` as inputs. This function inserts `x` into the correct position in the sorted stack.
2. In the `sortStack` function:
   - If the stack is not empty, pop the top element.
   - Recursively call `sortStack` to sort the remaining stack.
   - Use the `insert` function to insert the popped element back into the sorted stack.

### Time Complexity
The time complexity is \(O(n^2)\), where \(n\) is the number of elements in the stack. This is because for each element, we might need to traverse the entire stack to find its correct position.

### Space Complexity
The space complexity is \(O(n)\), due to the recursion stack used for sorting and inserting elements.

### Algorithm
1. Define the `insert` function:
   - If the stack is empty or the top of the stack is less than or equal to `x`, push `x` onto the stack.
   - Otherwise, pop the top element, recursively call `insert` with the remaining stack and `x`, then push the popped element back.

2. In the `sortStack` function:
   - If the stack is not empty, pop the top element.
   - Recursively call `sortStack` to sort the remaining stack.
   - Call `insert` to insert the popped element back into the sorted stack.
"""

def sortStack(stack):
    def insert(stack, x):
        if len(stack) == 0 or stack[-1] <= x:
            stack.append(x)
        else:
            temp = stack.pop()
            insert(stack, x)
            stack.append(temp)
            
    if len(stack):
        x = stack.pop()
        sortStack(stack)
        insert(stack, x)
