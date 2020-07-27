def spiralOrder(matrix):
    lo_m, hi_m = 0, len(matrix)-1
    lo_n, hi_n = 0, len(matrix[0])-1
    length = len(matrix)*len(matrix[0])
    res = []
    while len(res) < length:
        i = lo_m
        for j in range(lo_n, hi_n+1):
            res.append(matrix[i][j])
        if len(res) == length:
            break
        lo_m += 1
        j = hi_n
        for i in range(lo_m, hi_m+1):
            res.append(matrix[i][j])
        if len(res) == length:
            break
        hi_n -= 1
        i = hi_m
        for j in range(hi_n, lo_n-1, -1):
            res.append(matrix[i][j])
        if len(res) == length:
            break
        hi_m -= 1
        j = lo_n
        for i in range(hi_m, lo_m-1, -1):
            res.append(matrix[i][j])
        lo_n += 1
    return res
