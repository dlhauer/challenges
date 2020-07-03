def dailyTemperatures(T):
    stack = []
    for i, temp in enumerate(T):
        while len(stack) and stack[-1][1] < temp:
            prev = stack.pop()
            T[prev[0]] = i - prev[0]
        stack.append((i, temp))
    for day, _ in stack:
        T[day] = 0
    return T 

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))
