import collections

def ladderLength(beginWord, endWord, wordList):

    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    
    def getBaseForms(s):
        return [s[:i]+'_'+s[i+1:] for i in range(len(s))]

    combos = collections.defaultdict(list)
    for word in wordList:
        for form in getBaseForms(word):
            combos[form].append(word)

    q = collections.deque([(beginWord, 1)])
    visited = set(beginWord)
    while q:
        word, level = q.pop()
        if word == endWord:
            return level
        for form in getBaseForms(word):
            for word in combos[form]:
                if word not in visited:
                    q.appendleft((word, level+1))
                    visited.add(word)
            combos.pop(form)
    return 0
