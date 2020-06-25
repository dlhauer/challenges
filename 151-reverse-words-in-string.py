def reverseWordsOne(s):
    s = s.split(' ')
    s.reverse()
    return ' '.join([word for word in s if len(word) >= 1])

def reverseWordsTwo(s):
    res = ''
    i = -1
    while i >= -len(s):
        while i >= -len(s) and s[i] == ' ':
            i -= 1
        j = i
        while j >= -len(s) and s[j] != ' ':
            j -= 1
        if i == -1:
            word = s[j+1:]
        else:
            word = s[j+1:i+1]
        if word:
            res += word+' '
        i = j
    return res[:-1]




s = '     a    good   example    '
print(reverseWordsTwo(s), len(reverseWordsTwo(s)))