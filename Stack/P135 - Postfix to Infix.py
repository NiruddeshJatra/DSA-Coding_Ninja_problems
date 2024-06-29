"""
### Problem
Convert a postfix expression to an infix expression.

### Intuition
In postfix notation, operands precede their operators. The goal is to convert this format into infix notation, where operators are between operands.

### Approach
1. **Use a Stack**:
   - Iterate through each character in the input string.
   - If the character is an operand (alphanumeric), push it onto the stack.
   - If the character is an operator, pop the top two elements from the stack, form an infix expression with the operator between them, and push the resulting expression back onto the stack.
2. **Output**:
   - The final result will be the only element left in the stack.

### Time Complexity
O(n), where n is the length of the string. Each character is processed once.

### Space Complexity
O(n), due to the stack used to store intermediate results.

### Code
"""

class Solution:
    def postToInfix(self, s):
        stack = []

        for c in s:
            if c.isalnum():
                stack.append(c)
            else:
                second = stack.pop()
                first = stack.pop()
                exp = '(' + first + c + second + ')'
                stack.append(exp)
            
        return stack[0]
