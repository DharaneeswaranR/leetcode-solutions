class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[j - 1] == nums2[i - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])

        return res
    

"""
Approach: Dynamic Programming

- This problem is a variation of Longest Common Subsequence and is same as Longest Common Substr
- dp[i][j] represents the length of the longest subarray that ends with nums1[i-1] and nums2[j-1]

"""