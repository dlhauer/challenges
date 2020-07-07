def getLiveNeighbors(board, i, j):
    neighbors = 0
    for k in range(i-1, i+2):
        if k < 0 or k > len(board)-1:
            continue
        for l in range(j-1, j+2):
            if l < 0 or l > len(board[i])-1:
                continue
            if (k, l) != (i, j):
                if 1 <= board[k][l] <= 2:
                    neighbors += 1
    return neighbors

def gameOfLife(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            live_neighbors = getLiveNeighbors(board, i, j)
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = 2
            elif board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 3
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2:
                board[i][j] = 0
            elif board[i][j] == 3:
                board[i][j] = 1
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

gameOfLife(board)
print(board)
