import numpy as np
import os, sys

def searchInsert(nums, target):
    n = len(nums)
    if n == 1:
        return nums[0]
    else:
        nby2 = int(n/2)
        print(f'nby2: {nby2}, nums: {nums}, nums[nby2:]:{nums[nby2:]}, nums[:nby2]:{nums[:nby2]}')
        if nums[nby2] == target:
            close = searchInsert([nums[nby2]],target)
        elif nums[nby2] < target:
            close = searchInsert(nums[nby2:],target)
        else:
            close = searchInsert(nums[:nby2],target)
    return close

print(searchInsert([1,3,5,6],7))