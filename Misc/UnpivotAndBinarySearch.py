import numpy as np
import os, sys

def search(nums, target):
    pivot_elem = search_pivot_elem(nums)

def search_index(nums, target, indx=0):
    try:
        if nums[indx] == target:
            return indx
        else:
            search_index(nums, target, indx+1)
    except:
        return -1
        #raise IndexError
def search_max_elem(num):
    try:
        pass
    except:
        pass

def search_pivot_elem(nums):
    n = len(nums)
    nby2 = int(n/2)
    if n == 1: return nums[0]
    elif nums[nby2] > nums[nby2+1]:
        search_pivot_elem(nums[nby2:])
    elif nums[nby2] < nums[nby2-1]:
        search_pivot_elem(nums[nby2:])
    else:
        pass

print(search([4,5,6,7,0,1,2], 7))