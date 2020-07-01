def getComparison(num1, num2):
    if num1 > num2:
        return 'greater'
    elif num1 < num2:
        return 'less'
    else:
        return None

def maxTurbulenceSize(A):
    if len(A) == 2 and A[0] != A[1]:
        return len(A)
    elif len(set(A)) == 1:
        return 1
    max_len, i, j = 0, 0, 1
    while j < len(A)-1:
        prev_comp = getComparison(A[j-1], A[j])
        if (prev_comp == 'less' and A[j] > A[j+1]) or (prev_comp == 'greater' and A[j] < A[j+1]):
            pass
        else:
            i = j
        j += 1
        max_len = max(max_len, j-i+1)
    return max_len
arr = [4,4,5,4]
print(maxTurbulenceSize(arr))