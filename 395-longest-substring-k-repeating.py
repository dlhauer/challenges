import collections

def longestSubstring(s, k):
    max_len = 0
    q = collections.deque()
    q.append(s)
    while q:
        sub_str = q.pop()
        if sub_str == '':
            continue
        count = collections.Counter(sub_str)
        if min(count.values()) >= k:
            max_len = max(max_len, sum(count.values()))
            continue
        q.extendleft(sub_str.split([key for key in count if count[key] < k][0]))
    return max_len
