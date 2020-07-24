def lengthOfLongestSubstring(s):
    used = dict()
    max_len = i = 0
    for j, char in enumerate(s):
        if char in used and used[char] >= i:
            i = used[char]+1
        else:
            max_len = max(max_len, j-i+1)
        used[char] = j
    return max_len

s = 'acbabcbbdefg'
print(lengthOfLongestSubstring(s))