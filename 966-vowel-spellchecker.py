def vowelStrip(s):
    res = ''
    for char in s:
        if char in 'aeiou':
            res += '*'
        else:
            res += char
    return res

def getWordTable(wordlist):
    word_table = dict()
    for word in wordlist:
        key = vowelStrip(word.lower())
        if key in word_table:
            word_table[key].append(word)
        else:
            word_table[key] = [word]
    return word_table

def spellChecker(wordlist, queries):
    word_table = getWordTable(wordlist)
    res = []
    for query in queries:
        key = vowelStrip(query.lower())
        if key in word_table:
            if query in word_table[key]:
                res.append(query)
            else:
                found = False
                for word in word_table[key]:
                    if word.lower() == query.lower():
                        res.append(word)
                        found = True
                        break
                if found:
                    continue
                for word in word_table[key]:
                    if vowelStrip(word.lower()) == vowelStrip(query.lower()):
                        res.append(word)
                        break
        else:
            res.append('')
    return res


wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto", 'hero', 'HERO', 'HR', 'hiRu', 'Hare']
print(spellChecker(wordlist, queries))
