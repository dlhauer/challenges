import math
def canArrange(arr, k):
    remainders = [0]*k
    for num in arr:
        remainders[num%k] += 1
    if remainders[0] % 2 != 0:
        return False
    for i in range(1, math.ceil(len(remainders)/2)):
        if remainders[i] != remainders[k-i]:
            return False
    return True
