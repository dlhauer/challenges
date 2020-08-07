def searchRange(nums, target):

    def find_left(lo, hi):
        while lo <= hi:
            mid = (hi+lo) // 2
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                return mid
            elif nums[mid] == target:
                hi = mid-1
            elif nums[mid] != target:
                lo = mid+1
        return None
    
    def find_right(lo, hi):
        while lo <= hi:
            mid = (hi+lo) // 2
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target):
                return mid
            elif nums[mid] == target:
                lo = mid+1
            elif nums[mid] != target:
                hi = mid-1
        return None

    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (hi+lo) // 2
        if nums[mid] == target:
            return [find_left(lo, mid), find_right(mid, hi)]
        elif nums[mid] < target:
            lo = mid+1
        elif nums[mid] > target:
            hi = mid
    return [-1, -1]
