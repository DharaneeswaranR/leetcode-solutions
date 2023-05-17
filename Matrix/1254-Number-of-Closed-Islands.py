class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i == rows or j == cols:
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            """
            we dont use return dfs(g, i+1, j) && dfs(g, i, j+1) && dfs(g, i-1, j) && dfs(g,  i, j-1)
            BECAUSE IF ANY OF THE FIRST DFS() RETURNS FALSE, FOLLOWING ONES WILL NOT EXECUTE!!! THEN WE DON'T
            HAVE THE CHANCE TO MARK THOSE 0s TO 1s leading to partially dfs island
            """
            left = dfs(i, j-1)
            top = dfs(i-1, j)
            right = dfs(i, j+1)
            bottom = dfs(i+1, j)
            return left and top and right and bottom

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        res += 1

        return res