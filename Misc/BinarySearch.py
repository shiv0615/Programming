"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    n = len(input_array)
    if n == 1:
        if input_array[0] == value: return True
        else: return False
    elif n == 2:
        if input_array[0] == value or input_array[1] == value: return True
        else: return False
    else:
        bool_left  = binary_search(input_array[:int(n/2)], value)
        bool_right = binary_search(input_array[int(n/2):], value)
        bool = bool_left or bool_right
    return bool

class Solution:
    def search(self, nums, target):
        if len(nums) == 0: return -1
        indx_left = 0
        indx_right = len(nums)
        def search_recursively(self, nums, target, indx_left, indx_right):
            n = len(nums[indx_left:indx_right])
            if n<=1:
                if nums[indx_left] == target: return indx_left
                else: return -1
            else:
                nby2 = int((indx_left + indx_right)/2)
                if nums[nby2] > target:
                    indx_right = nby2
                else:
                    indx_left = nby2
                indx = search_recursively(self, nums, target, indx_left, indx_right)
                return indx
        return search_recursively(self, nums, target, indx_left, indx_right)

class Solution_2:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))