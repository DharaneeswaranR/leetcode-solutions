class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val -> index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            
            hashmap[n] = i

"""
Approach:

Naive - We can use bruteforce approach using to nested loops to find which two numbers
adds to the target.

Using Hashmap -

diff = target - n

We can use hashmap to store the difference(key) and index(val) and search
if the difference is present in the hashmap.

Time hashmaplexity - O(n)

"""