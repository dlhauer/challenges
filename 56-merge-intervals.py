def merge(intervals):
    if not intervals:
        return []
    intervals.sort()
    res = []
    prev = intervals[0]
    for i in range(1, len(intervals)):
        if prev[0] <= intervals[i][0] <= prev[1]:
            intervals[i] = [prev[0], max(intervals[i][1], prev[1])]
        else:
            res.append(prev)
        prev = intervals[i]
    res.append(intervals[-1])
    return res
