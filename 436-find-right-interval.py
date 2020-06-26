def findMin(intervals, start):
    low, high = 0, len(intervals)
    res = -1
    while low < high:
        mid = (low+high)//2
        if intervals[mid][0] >= start:
            res = mid
            high = mid
        else:
            low = mid+1
    return intervals[res] if res != -1 else res

def findRightInterval(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    for i, interval in enumerate(sorted_intervals):
        right = findMin(sorted_intervals[i+1:], sorted_intervals[i][1])
        intervals[intervals.index(interval)] = intervals.index(right) if right != -1 else right
    return intervals

intervals = [[5,7],[7,8],[1,4],[2,3],[6,9],[3,4]]
print(findRightInterval(intervals))