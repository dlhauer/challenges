def canJump(nums):
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

nums = [i for i in range(25000,0,-1)]
nums.append(0)
nums.append(1)
print(canJump(nums))
