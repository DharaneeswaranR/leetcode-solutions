class Solution:
    def uniquePaths(self, m: int, n: int) -> int:         
        rows = [[1] * n] * m

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                rows[i][j] = rows[i+1][j] + rows[i][j+1]
      
        return rows[0][0]


"""
Approach: Dynamic Programming

Consider the following memorization matrix for 3 x 7 grid

+----+----+----+----+---+---+---+
| 28 | 21 | 15 | 10 | 6 | 3 | 1 |
+----+----+----+----+---+---+---+
|  7 |  6 |  5 |  4 | 3 | 2 | 1 |
+----+----+----+----+---+---+---+
|  1 |  1 |  1 |  1 | 1 | 1 | 1 |
+----+----+----+----+---+---+---+

1) If the robot is anywhere in the last column or row, it has one path to reach
   the bottom right corner.
   right -> right -> right -> ... (or)
   down -> down -> down -> ...

2) If the robot is anywhere other than the last column or row lets assume r[i][j]
   , it has sum of r[i+1][j] + r[i][j+1] paths to reach the bottom corner.

3) So the total number of unique paths will be in r[0][0]


"""