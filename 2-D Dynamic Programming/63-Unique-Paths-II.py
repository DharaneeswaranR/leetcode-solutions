class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:     # if obstacle, no paths
                    dp[i][j] = 0
                elif i == m - 1 and j == n - 1: # if destination, 1 path
                    dp[i][j] = 1
                elif i == m - 1:                # if bottom row
                    dp[i][j] = dp[i][j+1]
                elif j == n - 1:                # if right edge
                    dp[i][j] = dp[i+1][j] 
                else:
                    dp[i][j] = dp[i][j+1] + dp[i+1][j]

        return dp[0][0]
    

"""
Approach: Dynamic programming

Similar to leetcode 62. Unique Paths with some extra cases to handle

"""