def numJewelsInStones(J, S):
    return len([stone for stone in S if stone in J])

J = ''
S = 'aa'
print(numJewelsInStones(J, S))
