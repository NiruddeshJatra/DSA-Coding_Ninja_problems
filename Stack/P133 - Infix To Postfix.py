"""
### Problem
Convert an infix expression to a postfix expression (Reverse Polish Notation).

### Intuition
Infix expressions are difficult for computers to parse due to operator precedence and parentheses. Postfix notation eliminates the need for parentheses and clarifies the order of operations.

### Approach
1. **Precedence Dictionary**:
   - Define operator precedence levels in a dictionary.
2. **Initialization**:
   - Use an empty list `ans` to hold the output.
   - Use a stack to manage operators and parentheses.
3. **Iterate Through Expression**:
   - If the character is an operand (alphanumeric), append it to `ans`.
   - If the character is `(`, push it onto the stack.
   - If the character is `)`, pop from the stack to `ans` until a `(` is encountered.
   - For operators, pop from the stack to `ans` based on precedence, then push the current operator onto the stack.
4. **Finalize**:
   - After processing all characters, pop any remaining operators from the stack to `ans`.
5. **Output**:
   - Join and return the `ans` list as a string.

### Time Complexity
O(n), where n is the length of the expression. Each character is processed once.

### Space Complexity
O(n), due to the stack and the output list.

### Code
"""

def infixToPostfix(exp):
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
    return "".join(ans)
