"""
### Problem
Given a stack, reverse its elements such that the bottom element becomes the top element. You can only use standard stack operations (push, pop, isEmpty, and isFull).

### Intuition
The problem can be solved using a recursive approach. The idea is to recursively pop elements from the stack until it is empty, then insert the popped elements at the bottom of the stack in reverse order.

### Approach
1. Define a helper function `insertAtBottom` that takes a stack and an element `x` as inputs. This function inserts `x` at the bottom of the stack.
2. In the `reverseStack` function:
   - If the stack is not empty, pop the top element.
   - Recursively call `reverseStack` to reverse the remaining stack.
   - Use the `insertAtBottom` function to insert the popped element at the bottom of the reversed stack.

### Time Complexity
The time complexity is \(O(n^2)\), where \(n\) is the number of elements in the stack. This is because for each element, we might need to traverse the entire stack to insert it at the bottom.

### Space Complexity
The space complexity is \(O(n)\), due to the recursion stack used for reversing the elements.

### Algorithm
1. Define the `insertAtBottom` function:
   - If the stack is empty, push `x` onto the stack.
   - Otherwise, pop the top element, recursively call `insertAtBottom` with the remaining stack and `x`, then push the popped element back.

2. In the `reverseStack` function:
   - If the stack is not empty, pop the top element.
   - Recursively call `reverseStack` to reverse the remaining stack.
   - Call `insertAtBottom` to insert the popped element at the bottom of the reversed stack.
"""

def reverseStack(stack):
    def insertAtBottom(stack, x):
        if len(stack) == 0:
            stack.append(x)
        else:
            temp = stack.pop()
            insertAtBottom(stack, x)
            stack.append(temp)

    if len(stack):
        temp = stack.pop()
        reverseStack(stack)
        insertAtBottom(stack, temp)
