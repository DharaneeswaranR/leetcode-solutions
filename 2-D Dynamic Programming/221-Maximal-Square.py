class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        maximum = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == "0":
                    dp[i][j] == 0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maximum = max(maximum, dp[i][j])

        return maximum * maximum
    

"""
Approach: Dynamic Programming

Given Matrix

+---+---+---+---+---+
| 1 | 0 | 1 | 0 | 0 |
+---+---+---+---+---+
| 1 | 0 | 1 | 1 | 1 |
+---+---+---+---+---+
| 1 | 1 | 1 | 1 | 1 |
+---+---+---+---+---+
| 1 | 0 | 0 | 1 | 0 |
+---+---+---+---+---+

DP Matrix

+---+---+---+---+---+---+
| 0 | 0 | 0 | 0 | 0 | 0 |       
+---+---+---+---+---+---+       
| 0 | 1 | 0 | 1 | 0 | 0 |
+---+---+---+---+---+---+
| 0 | 1 | 0 | 1 | 1 | 1 |
+---+---+---+---+---+---+
| 0 | 1 | 1 | 1 | 2 | 2 |
+---+---+---+---+---+---+
| 0 | 1 | 0 | 0 | 1 | 0 |
+---+---+---+---+---+---+


Zero : 0
One  : min(top, left, top-left) + 1

- Create a 2D array of size (m + 1) * (n + 1)
- For each cell, we can either be 0 or 1.
- If the cell is 1, then we can calculate the size of the square that can be formed starting from that cell.
- We can do this by finding the minimum of the top, left, and top-left cells.
- We can then add 1 to that minimum to get the size of the square that can be formed starting from that cell.
- We can then compare this size to our global maximum and update it if necessary.
- We can then continue this process for all cells in the matrix.
- Finally, we return the global maximum.

Time Complexity: O(m * n)
Space Complexity: O(m * n)

"""