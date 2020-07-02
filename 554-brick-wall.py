def leastBricks(wall: List[List[int]]) -> int:
    length_map = dict()
    one_brick = True
    max_flush = 0
    for row in wall:
        if len(row) > 1:
            one_brick = False
        for j in range(len(row)-1):
            cur_sum = sum(row[:j+1])
            if cur_sum in length_map:
                length_map[cur_sum] += 1
                max_flush = max(max_flush, length_map[cur_sum])
            else:
                length_map[cur_sum] = 1
    least_bricks = len(wall) - max_flush
    if least_bricks < len(wall):
        return least_bricks
    elif one_brick:
        return len(wall)
    else: 
        return least_bricks-1
