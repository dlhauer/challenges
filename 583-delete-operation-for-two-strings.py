def minDistance(s1, s2):
    memo = [([0]*len(s2)).copy() for _ in range(len(s1))]

    def lcs_helper(s1, s2, i, j):
        if i < 0 or j < 0:
            return 0
        if memo[i][j] > 0:
            return memo[i][j]
        if s1[i] == s2[j]:
            memo[i][j] = 1 + lcs_helper(s1, s2, i-1, j-1)
        else:
            memo[i][j] = max(lcs_helper(s1, s2, i-1, j), lcs_helper(s1, s2, i, j-1))
        return memo[i][j]
    
    return len(s1) + len(s2) - (2 * lcs_helper(s1, s2, len(s1)-1, len(s2)-1))
