class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        
        while left < right:
            while left < right and nums[left] % 2 == 0:
                left += 1
            while left < right and nums[right] % 2 != 0:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        
        return nums


"""
Approach: Two Pointers

Create two pointers pointing the ends of the array. If the left pointer is odd and right pointer
is even, swap.

"""