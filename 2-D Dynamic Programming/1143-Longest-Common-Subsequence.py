class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
    

"""
Approach: Dynamic Programming

DP Matrix

+---+---+---+---+---+---+---+---+---+
| . | . | x | a | b | c | c | d | e |
+---+---+---+---+---+---+---+---+---+
| . | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
+---+---+---+---+---+---+---+---+---+
| a | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
+---+---+---+---+---+---+---+---+---+
| c | 0 | 0 | 1 | 1 | 2 | 2 | 2 | 2 |
+---+---+---+---+---+---+---+---+---+
| e | 0 | 0 | 1 | 1 | 2 | 2 | 2 | 3 |
+---+---+---+---+---+---+---+---+---+

"""