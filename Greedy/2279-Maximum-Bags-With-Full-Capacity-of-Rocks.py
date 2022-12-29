class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        full_bags = 0

        for i in range(len(capacity)):
            capacity[i] -= rocks[i]

        capacity.sort()

        for c in capacity:
            if c <= additionalRocks:
                additionalRocks -= c 
                full_bags += 1
            else:
                break

        return full_bags


"""
Approach: Greedy

1. Find the remaining capacity after rocks are filled capacity[i] - rocks[i]
2. Sort the remaining capacity in increasing order so that the maximum number of 
   bags can be filled with additional rocks.
   
"""