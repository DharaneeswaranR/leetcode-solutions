class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Base cases
        one_step_before = 1
        two_step_before = 2
        total_ways = 0

        for i in range(2, n):
            total_ways = one_step_before + two_step_before
            one_step_before = two_step_before
            two_step_before = total_ways

        return total_ways

    
"""
Approach: Dynamic Programming

Base cases

1. To reach nth step from (n-1)th step, there is 1 way (1 step)
2. To reach nth step from (n-2)th step, there are 2 ways (2 step, 1 step)

Explaination: 

Refer - https://leetcode.com/problems/climbing-stairs/solutions/25299/basically-it-s-a-fibonacci/

"""