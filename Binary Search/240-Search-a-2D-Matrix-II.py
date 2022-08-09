class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        
        row, col = 0, len(matrix[0]) - 1
        
        while (row < len(matrix) and col >= 0):
            if target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            else:
                return True
            
        return False


"""
Approach:

We can treat this matrix as a binary search tree if we start from either top-right or
bottom-left as each row and col is sorted. Apply the same logic of finding an element 
in BST to the matrix.

if the target is greater than the value in current position, then the target can not be
in entire row of current position because the row is sorted, if the target is less than 
the value in current position, then the target can not in the entire column because the 
column is sorted too. 
(credits: https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66140/My-concise-O(m%2Bn)-Java-solution)

"""
            