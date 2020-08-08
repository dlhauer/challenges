import math

def evalRPN(tokens):
    stack = []
    op_map = {
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: x//y if x/y >= 0 else math.ceil(x/y)
    }
    for token in tokens:
        if token in '+-*/':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op_map[token](op1, op2))
        else:
            stack.append(int(token))
    return int(stack[0])
