def findMin(nums):
    lo, hi = 0, len(nums)-1
    while lo < hi:
        mid = (hi+lo)//2
        if nums[lo] <= nums[mid] < nums[hi]:
            break
        elif nums[lo] > nums[mid] < nums[hi]:
            if 0 <= mid < len(nums) and nums[mid-1] > nums[mid] < nums[mid+1]:
                return nums[mid]
            hi = mid-1
        elif nums[lo] <= nums[mid] > nums[hi]:
            lo = mid+1
    return nums[lo]
