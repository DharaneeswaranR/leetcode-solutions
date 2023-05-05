class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y, x = heapq.heappop(stones), heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, y - x)
        
        return stones[0] * -1 if stones else 0
    
"""
Approach: Max Heap

As python deoesn't support max-heap we multiply weights of stones to negative to create max-heap

"""