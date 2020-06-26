def findLength(A, B):
    dp = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
    max_len = 0
    for i in range(len(A)-1, -1, -1):
        for j in range(len(B)-1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            max_len = max(max_len, dp[i][j])
    for row in dp:
        print(row)
    return max_len

A = [1,4,3,7]
B = [7,1,3,4,3]

print(findLength(A, B)) 
