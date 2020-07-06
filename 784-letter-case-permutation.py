def letterCasePermutation(S):
    if len(S) == 0:
        return ['']
    heads = set([S[0].upper(), S[0].lower()])
    return [head + tail for tail in letterCasePermutation(S[1:]) for head in heads]

S = 'ab12c'
print(letterCasePermutation(S))
