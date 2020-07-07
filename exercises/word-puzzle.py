def read_dictionary(filename='c06d'):
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

def word_puzzle():
    pron = read_dictionary('./pron-dictionary.txt')
    fin = open('./words.txt')
    fives, fours, res, = set(), set(), set()
    for line in fin:
        t = line.split()
        word = t[0]
        if len(word) == 5:
            fives.add(word)
        elif len(word) == 4:
            fours.add(word)
    for word in fives:
        rem1 = word[1:]
        rem2 = word[:1] + word[2:]
        if (rem1 in fours and rem2 in fours
        and word in pron and rem1 in pron and rem2 in pron
        and pron[word] == pron[rem1]
        and pron[word] == pron[rem2]):
            res.add(word)
    return res

print(word_puzzle())
