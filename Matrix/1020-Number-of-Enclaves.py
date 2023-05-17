class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        moves = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i == rows or j == cols or grid[i][j] == 0:
                return
            grid[i][j] = 0
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)

        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows - 1 or j == cols - 1) and grid[i][j] == 1:
                    dfs(i, j)
        
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if grid[i][j] == 1:
                    moves += 1

        return moves
    
"""
Approach : DFS

Use DFS to traverse the boundary of the grid and mark the visited nodes as 0 (Sink the island).
Then traverse the rest of the grid and count the number of 1s.
"""