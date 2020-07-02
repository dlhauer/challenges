
def isPredecessor(word, pred):
    for char in pred:
        if char not in word:
            return False
        word = word.replace(char, '', 1)
    return len(word) == 1

def longestStrChain(words):
    chains = {1:set()}
    for word in words:
        if len(word) == 1:
            chains[1].add(word)
            continue
        found = False
        for i in range(len(word)-1, 0, -1):
            if i in chains:
                for pred in chains[i]:
                    if isPredecessor(word, pred):
                        found = True
            if found:
                if i+1 in chains:
                    chains[i+1].add(word)
                else:
                    chains[i+1] = {word}
                break
        if not found:
            chains[1].add(word)
    return max(chains.keys())

words = ["bdxca","a","b","ba","bca","bda","bdca", "bdxcal"]
print(longestStrChain(words))
