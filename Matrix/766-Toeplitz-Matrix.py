class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                
        return True

"""
Traverse the matrix and check if nearest bottom right element is same are current element

"""