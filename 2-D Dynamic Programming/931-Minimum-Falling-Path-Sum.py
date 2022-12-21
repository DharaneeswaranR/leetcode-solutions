class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = cols = len(matrix)

        for i in range(1, rows):
            for j in range(cols):
                if j == 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1])
                elif j == cols - 1:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j-1])
                else:
                    matrix[i][j] += min(matrix[i-1][j+1], matrix[i-1][j], matrix[i-1][j-1])
        
        return min(matrix[-1])
        
        
"""
Approach Dynamic programming

Input:

+---+---+---+
| 2 | 1 | 3 |
+---+---+---+
| 6 | 5 | 4 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+

DP Matrix:

+----+----+----+
|  2 |  1 |  3 |
+----+----+----+
|  7 |  6 |  5 |
+----+----+----+
| 13 | 13 | 14 |
+----+----+----+

Top-down approach - start from 2nd row and find the smallest element in previous row that is 
either directly above or diagonally left/right. Add this smallest element with current element
in dp matrix. The smallest element from last row gives minimum sum.

"""