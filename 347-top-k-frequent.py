import collections
import random

def topKFrequent(nums, k):
    count = collections.Counter(nums)
    unique = list(count.keys())
    n = len(unique)
    if k == n:
        return unique

    def partition(left, right, pivot_index):
        pivot_frequency = count[unique[pivot_index]] 
        store_index = left
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

        for i in range(left, right):
            if count[unique[i]] < pivot_frequency:
                unique[i], unique[store_index] = unique[store_index], unique[i]
                store_index += 1
        unique[right], unique[store_index] = unique[store_index], unique[right]
        
        return store_index

    def quickSelect(left, right):
        pivot_index = random.randint(left, right)
        part = partition(left, right, pivot_index)
        if part == n-k:
            return
        elif part < n-k:
            quickSelect(part+1, right)
        else:
            quickSelect(left, part-1)

    quickSelect(0, len(unique)-1)
    return unique[n-k:]
