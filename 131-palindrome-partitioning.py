def partition(s):
    res = []

    def isPalindrome(s):
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        else:
            return False

    def helper(s, path=[]):
        if not s:
            res.append(path)
        for i in range(len(s)):
            if isPalindrome(s[0:i+1]):
                helper(s[i+1:], path+[s[0:i+1]])
    helper(s)
    return res
