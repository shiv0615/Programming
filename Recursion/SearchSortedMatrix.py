'''
https://leetcode.com/problems/search-a-2d-matrix-ii/solution/
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def BinarySearch(array, target):
            if len(array) == 0: return False
            mid = len(array) // 2
            if array[mid] == target:
                return True
            else:
                if array[mid] > target:
                    return BinarySearch(array[:mid], target)
                elif array[mid] < target:
                    return BinarySearch(array[mid + 1:], target)

        for col in range(len(matrix)):
            if BinarySearch(matrix[col], target):
                return True

        return False