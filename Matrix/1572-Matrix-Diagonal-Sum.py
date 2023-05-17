class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        rows, cols = len(mat), len(mat[0])

        for i in range(rows):
            res += mat[i][i]
            res += mat[i][cols - i - 1]
        
        # if square matrix, the mat[rows//2][cols//2] will be added twice hence we subtract once
        if rows % 2 != 0:
            res -= mat[rows//2][cols//2]

        return res
