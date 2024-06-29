def postfixToPrefix(s: str) -> str:
    def postToInfix(s):
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

    infix = postToInfix(s)
    return infixToPrefix(infix)

    
