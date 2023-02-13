class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1 == 0: # is even using bit wise
            return (high - low + 1) // 2
        return (high - low) // 2 + 1 



