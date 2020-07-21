def subsetsWithDup(nums):
    output = set()
    output.add(())
    nums.sort()
    for i, num in enumerate(nums):
        temp = output.copy()
        for sub in temp:
            output.add(sub + (num,))
    return [list(tup) for tup in output]

nums = [1,2,2]
print(subsetsWithDup(nums))
