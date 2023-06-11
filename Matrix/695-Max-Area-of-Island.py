class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        max_area = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i == r or j == c or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1)
            
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area