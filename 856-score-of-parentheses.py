def scoreOfParentheses(S):
    stack = [0]
    for i, paren in enumerate(S):
        if paren == '(':
            stack.append(0)
        elif S[i-1] == '(':
            stack.pop()
            stack[-1] += 1
        else:
            val = stack.pop()
            stack[-1] += val * 2
    return stack[0]

s = '(())()()'
print(scoreOfParentheses(s))