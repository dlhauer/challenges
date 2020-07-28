def permute(nums):
    res = []

    def helper(nums, path=[]):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            helper(nums[:i]+nums[i+1:], path+[nums[i]])

    helper(nums)
    return res
