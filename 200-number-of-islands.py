import collections

def getNeighbors(mat, i, j):
    if i > len(mat)-1 or j > len(mat[0])-1:
        return None
    res = []
    if i > 0:
        res.append((i-1, j))
    if i < len(mat)-1:
        res.append((i+1, j))
    if j > 0:
        res.append((i, j-1))
    if j < len(mat[0])-1:
        res.append((i, j+1))
    return res

def numIslands(grid):
    islands = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                islands += 1
                queue = collections.deque()
                queue.appendleft((i, j))
                while queue:
                    x, y = queue.pop()
                    grid[x][y] = '#'
                    neighbors = getNeighbors(grid, x, y)
                    for a, b in neighbors:
                        if grid[a][b] == '1' and (a, b) not in visited:
                            visited.add((a, b))
                            queue.appendleft((a,b))
    return islands
