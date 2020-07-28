def canJump1(nums):
    start_points = dict()

    def helper(start):
        if nums[start] >= len(nums)-start-1:
            return True
        if start > len(nums)-1:
            return False
        if start not in start_points:
            start_points[start] = any([helper(start+i+1) for i in range(0, nums[start])])
        return start_points[start]

    return helper(0)

def canJump2(nums):
    last_pos = len(nums)-1
    for i in range(len(nums)-1, -1, -1):
        if i+nums[i] >= last_pos:
            last_pos = i
    return last_pos == 0
