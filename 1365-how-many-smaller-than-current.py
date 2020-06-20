def smallerNumbersThanCurrent(nums):
    res = [None] * len(nums)
    for i, num in enumerate(nums):
        res[i] = len([n for n in nums[0:i]+nums[i+1:] if n < num])
    return res

nums = [7,7,7,7] 
print(smallerNumbersThanCurrent(nums))