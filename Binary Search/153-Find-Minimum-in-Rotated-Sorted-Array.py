class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        if nums[left] < nums[right] or right == 0: # if array is not rotated or has single element then leftmost is the minimum
            return nums[0]
        
        # if the array is rotated
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if nums[left] < nums[mid]: # the min elem must be present after the mid elem
                left = mid + 1
            else:                      # the min elem must be present before the mid elem
                right = mid - 1


# Solution:

# In a roated array the minimum is present at the point just after the largest element in the array
# This can be used in the condition to find the min element



