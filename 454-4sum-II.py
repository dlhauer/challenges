import collections

def fourSumCount(A, B, C, D):
    total = 0
    ab_sums = collections.defaultdict(int)
    for a in A:
        for b in B:
            ab_sums[a+b] += 1
    for c in C:
        for d in D:
            total += ab_sums[-(c+d)]
    return total

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(fourSumCount(A, B, C, D))
            