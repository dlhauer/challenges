def exist(board, word):

    def getNeighborCoords(pos):
        i, j = pos
        res = []
        if i > 0:
            res.append((i-1, j))
        if i < len(board)-1:
            res.append((i+1, j))
        if j > 0:
            res.append((i, j-1))
        if j < len(board[0])-1:
            res.append((i, j+1))
        return res

    def dfs(word, start=(0,0), visited=set()):
        i, j = start
        if not word or word == board[i][j]:
            return True
        if start in visited or board[i][j] != word[0]:
            return False
        neighbors = getNeighborCoords((i, j))
        v = visited.copy()
        v.add((i,j))
        return any([dfs(word[1:], n, v) for n in neighbors])

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(word, (i, j)):
                return True
    return False
