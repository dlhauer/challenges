import string

def wordCount(file):
    words = set()
    fin = open(file)
    for line in fin:
        line_words = line.split(' ')
        for word in line_words:
            dash = '-' if '-' in word else '—'
            wo = word.split(dash)
            for w in wo:
                w = w.strip()
                w = w.strip(string.punctuation + '“”' + "’‘")
                if w:
                    words.add(w.lower())
    return len(words)

if __name__ == '__main__':
    print('Great Expectations: ', wordCount('great-expectations.txt'))
    print('Moby Dick: ', wordCount('moby-dick.txt'))
