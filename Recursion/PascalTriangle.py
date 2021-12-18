'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]

Constraints:

0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''
from functools import lru_cache
class Solution:
    def getRow(self, rowIndex: int):
        @lru_cache(2000)
        def dp(i,j):
            if i == 0 or j == 0 or i == j or j== rowIndex:
                return 1
            else:
                return (dp(i-1,j-1)+dp(i-1,j))
        return [dp(rowIndex,k) for k in range(rowIndex+1)]

rowIndex = 4
solve = Solution()
res = solve.getRow(rowIndex=rowIndex)
print(f'Result : {res}')