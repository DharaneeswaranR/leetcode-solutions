class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg_count += 1
        
        return 1 if neg_count % 2 == 0 else -1


"""
Approach: 

Product of an array of integers will be negative if number of negative integers is odd
else positive.

"""