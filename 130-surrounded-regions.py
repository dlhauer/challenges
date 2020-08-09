import collections

def solve(board):

    def get_neighbors(pos):
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

    def bfs(pos):
        if board[pos[0]][pos[1]] != 'O':
            return
        q = collections.deque([pos])
        visited = set()
        visited.add(pos)
        while q:
            i, j = q.pop()
            board[i][j] = '_'
            neighbors = get_neighbors((i, j))
            for n in neighbors:
                a, b = n
                if board[a][b] == 'O' and n not in visited:
                    q.appendleft(n)
                    visited.add(n)

    for i in range(len(board)):
        if i == 0 or i == len(board)-1:
            for j in range(len(board[i])):
                bfs((i, j))
        else:
            bfs((i, 0))
            bfs((i, len(board[i])-1))

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '_':
                board[i][j] = 'O'
