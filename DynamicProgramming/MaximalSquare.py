'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''
class Solution:
    def maximalSquare(self, matrix):
        nrows = len(matrix)
        ncols = len(matrix[0])
        istart = 0
        jstart = 0
        iend = 1
        jend = 1
        max_sq = 0
        while istart <= iend-1 and jstart <= jend-1:
            fac = int(matrix[istart][jend])*int(matrix[istart+1][jend])*\
                  int(matrix[iend][jstart+1])*int(matrix[iend][jstart+1])
            max_sq = max(max_sq,((jend - jstart) + (iend - istart))*fac)
            iend += 1
            jend += 1
            if fac == 0:
                istart+=1
                jstart+=1
        return max_sq


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
solve = Solution()
result = solve.maximalSquare(matrix)
print(f'Maximal Square: {result}')