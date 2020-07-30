def maxProduct(nums):

    def getMax(nums):
        max_prod, cur_prod = nums[0], 1
        for num in nums:
            if num == 0:
                cur_prod = 1
                max_prod = max(max_prod, 0)
            else:
                cur_prod *= num
                max_prod = max(max_prod, cur_prod)
        return max_prod

    reverse_nums = nums[::-1]
    return max(getMax(nums), getMax(reverse_nums))
