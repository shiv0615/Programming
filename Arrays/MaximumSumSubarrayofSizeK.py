'''
Problem Statement#
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
Try it yourself#
'''
def max_sub_array_of_size_k(k, arr):
    if len(arr) < k: return 0
    currsum = sum(arr[0:k])
    maxsum = currsum
    for i in range(1,len(arr)-k):
      currsum += (arr[i+k-1] - arr[i-1])
      maxsum = max(currsum,maxsum)
    return maxsum