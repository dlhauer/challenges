def smallestRepunitDivByK(K):
    if K % 2 == 0 or K % 5 == 0:
        return -1
    ones = '1' * len(str(K**2))
    while True:
        if int(ones) % K == 0:
            return len(ones)
        ones += '1'

print(smallestRepunitDivByK(85671))