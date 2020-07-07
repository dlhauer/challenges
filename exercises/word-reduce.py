class Reducer():
    def __init__(self):
        self.reducible = set()
        self.dictionary = set()
        fin = open('./words.txt')
        for line in fin:
            t = line.split()
            self.dictionary.add(t[0])

    def getChildren(self, word):
        return [word[:i]+word[i+1:] for i in range(len(word))]

    def isReducible(self, word):
        if word not in self.dictionary:
            return False
        if len(word) == 1 or word in self.reducible:
            return True
        children = self.getChildren(word)
        for child in children:
            if self.isReducible(child):
                self.reducible.add(word)
                return True

    def getMax(self):
        for word in self.dictionary:
            self.isReducible(word)
        return max(self.reducible, key=len)

reducer = Reducer()
print(reducer.getMax())
