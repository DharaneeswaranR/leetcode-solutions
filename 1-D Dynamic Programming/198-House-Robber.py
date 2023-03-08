class Solution:
    def rob(self, nums: List[int]) -> int:
        r1 = r2 = 0

        for num in nums:
            r1, r2 = max(r2 + num, r1), r1

        return r1


"""
Figure out recursive relation.

A robber has 2 options: 
a) rob current house i 
b) don't rob current house

If an option "a" is selected it means she can't rob previous i-1 house but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.
If an option "b" is selected the robber gets all the possible loot from robbery of i-1 and all the following buildings.
So it boils down to calculating what is more profitable:

Recursive relation:

rob(i) = max(rob(i - 2) + currentHouseValue, rob(i - 1))

Source: https://leetcode.com/problems/house-robber/solutions/156523/from-good-to-great-how-to-approach-most-of-dp-problems

"""