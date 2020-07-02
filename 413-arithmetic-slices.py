def tri(num):
    return num * (num+1) // 2

def numberOfArithmeticSlices(A):
    total, i, j = 0, 0, 2
    while j < len(A):
        while j < len(A) and A[j]-A[j-1] == A[j-1]-A[j-2]:
            j += 1 
        total += tri(j-i-2)
        j += 1
        i = j-2
    return total

arr = [1,2,3,4,10,12,14]
print(numberOfArithmeticSlices(arr))
