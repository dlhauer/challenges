def getNeighbors(pos, matrix):
    if pos[0]-1 < 0 or pos[1]-1 < 0:
        return [0,0,0]
    else:
        return [matrix[pos[0]][pos[1]-1], matrix[pos[0]-1][pos[1]], matrix[pos[0]-1][pos[1]-1]]


def countSquares(matrix):
    count = 0
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num == 1:
                neighbors = getNeighbors([i,j], matrix)
                matrix[i][j] += min(neighbors)
                count += matrix[i][j]
    return count

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

print(countSquares(matrix))
