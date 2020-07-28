import bisect
def searchMatrix(matrix, target):
    lo, hi = 0, len(matrix)
    while lo < hi:
        mid = (lo+hi)//2
        if matrix[mid][0] > target:
            hi = mid
        else:
            lo = mid+1
    up_bound = hi
    lo, hi = 0, up_bound
    while lo < hi:
        mid = (lo+hi)//2
        if matrix[mid][-1] >= target:
            hi = mid
        else:
            lo = mid+1
    lo_bound = lo
    for row in range(lo_bound, up_bound):
        target_idx = bisect.bisect_left(matrix[row], target)
        if matrix[row][target_idx] == target:
            return True
    return False
