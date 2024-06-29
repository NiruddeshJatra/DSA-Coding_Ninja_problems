"""
### Problem
Convert a prefix expression to an infix expression.

### Intuition
In prefix expressions, operators precede their operands. The goal is to convert this format into the more human-readable infix notation, where operators are between operands.

### Approach
1. **Reverse the String**:
   - Reverse the input string to process from right to left.
2. **Use a Stack**:
   - Iterate over each character:
     - If it's an operand (alphanumeric), push it onto the stack.
     - If it's an operator, pop the top two elements from the stack, form a string with the operator between them, and push the resulting expression back onto the stack.
3. **Output**:
   - The result will be the only element left in the stack.

### Time Complexity
O(n), where n is the length of the string. Each character is processed once.

### Space Complexity
O(n), due to the stack used to store intermediate results.

### Code
"""

def prefixToInfixConversion(s: str) -> str:
    s = s[::-1]
    stack = []

    for c in s:
        if c.isalnum():
            stack.append(c)
        else:  
            exp = '(' + stack.pop() + c + stack.pop() + ')'
            stack.append(exp)
        
    return stack[0]
