import random
def findKthLargest(nums, k, left=0, right=None):

    def partition(left, right, pivot_index):
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        for i in range(left, right):
            if nums[i] <= nums[right]:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        nums[left], nums[right] = nums[right], nums[left]
        return left

    if right is None:
        right = len(nums)-1
    partition_index = partition(left, right, random.randint(left, right))
    target = len(nums)-k
    if partition_index == target:
        return nums[target]
    elif partition_index < target:
        return findKthLargest(nums, k, partition_index+1, right)
    else:
        return findKthLargest(nums, k, left, partition_index-1)

nums = [3,2,3,1,2,4,5,5,6]
print(sorted(nums))
k = 6
print(findKthLargest(nums, k))
    