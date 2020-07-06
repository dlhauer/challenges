import math
def generateParenthesis(n):
    base = [{''}, {'()'}]
    for i in range(2, n+1):
        base.append(set())
        for string in base[i-1]:
            for j in range(math.ceil(len(string)/2)+1):
                pair = '()'
                base[i].add(string[:j] + pair + string[j:])
    return list(base[n])

print(generateParenthesis(10))