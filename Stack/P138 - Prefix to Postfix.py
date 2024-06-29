def prefixToPostfix(s: str) -> str:
    def prefixToInfix(s: str) -> str:
        s = s[::-1]
        stack = []
    
        for c in s:
            if c.isalnum():
                stack.append(c)
            else:  
                exp = '(' + stack.pop() + c + stack.pop() + ')'
                stack.append(exp)
            
        return stack[0]
    
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

    infix = prefixToInfix(s)
    return infixToPostfix(infix)
