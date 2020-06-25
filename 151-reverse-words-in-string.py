def reverseWords(s):
    s = s.split(' ')
    s.reverse()
    return ' '.join([word for word in s if len(word) >= 1])

s = '   hello world! '
print(reverseWords(s), len(reverseWords(s)))
