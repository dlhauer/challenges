import bisect

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    row_maxes = [row[-1] for row in matrix]
    target_row = bisect.bisect_left(row_maxes, target)
    if target_row == len(matrix):
        return False
    target_idx = bisect.bisect_left(matrix[target_row], target)
    return matrix[target_row][target_idx] == target
