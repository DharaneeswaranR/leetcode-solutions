class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
        

"""
Approach: DP

Identify the recurrence relation

mincost(i) = cost[i] + min(mincost(i-1), mincost(i-2))

"""