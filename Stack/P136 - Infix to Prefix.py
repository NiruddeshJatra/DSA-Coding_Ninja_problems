"""
### Problem
Convert an infix expression to a prefix expression.

### Intuition
In prefix notation, operators precede their operands. This involves reversing the input string and handling parentheses accordingly.

### Approach
1. **Reverse the Input**:
   - Reverse the input string and switch parentheses to help convert to postfix.
2. **Use a Stack**:
   - Iterate through each character.
   - If the character is an operand (alphanumeric), add it to the result.
   - If it is an operator, pop from the stack to the result until an operator of lower precedence is found.
   - Use a precedence map to manage operator precedence.
3. **Finalize**:
   - Reverse the resulting postfix expression to get the prefix.

### Time Complexity
O(n), where n is the length of the string. Each character is processed once.

### Space Complexity
O(n), due to the stack used to store operators.

### Code
"""

def infixToPrefix(s):
    exp = ""
    for c in s[::-1]:
        if c == "(":
            exp += ")"
        elif c == ")":
            exp += "("
        else:
            exp += c

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
    ans, stack = [], []

    for c in exp:
        if c.isalnum():
            ans.append(c)
        else:
            if c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    ans.append(stack.pop())
                stack.pop()
            else:
                while stack and precedence[c] <= precedence[stack[-1]]:
                    ans.append(stack.pop())
                stack.append(c)

    ans.extend(stack[::-1])
    postfix = "".join(ans)
    return postfix[::-1]
