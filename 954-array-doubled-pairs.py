def canReorderDoubled(A):
    A = sorted(A)
    i = 0
    while i < len(A):
        try:
            dub = A.index(A[i]*2 if A[i] >= 0 else A[i]/2)
        except ValueError:
            dub = -1
        if dub == -1:
            return False
        else:
            A.pop(dub)
            A.pop(i)
    return True
        
A = [4,-2,2,-4,-2]
print(canReorderDoubled(A))
