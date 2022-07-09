class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1            
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # if mid in left portion
            if nums[left] <= nums[mid]:
                # Target is present in right portion
                if target < nums[left] or target > nums[mid]: 
                    left = mid + 1
                # Target is present in left portion
                else:
                    right = mid - 1

            # if mid in right portion    
            else:
                # Target is present in left portion
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                # Target is present in right portion
                else:
                    left = mid + 1
                
        return -1


# Solution 2 - Applying binary search on both sides
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = self.find_mid(nums, 0, len(nums) - 1)                         # Find pivot
        l = self.binary_search(nums, target, 0, mid)                        # Apply BS on left sorted portion
        r = self.binary_search(nums, target, mid + 1, len(nums) - 1)        # Apply BS on right sorted portion
        
        if l != -1:
            return l
        elif r != -1:
            return r 
        else:
            return -1
    
    # Finding the pivot
    def find_mid(self, nums: List[int], left, right) -> int:        
        if nums[left] < nums[right] or right == 0: 
            return 0
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid - 1] > nums[mid]:
                return mid - 1
            
            if nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[left] < nums[mid]: 
                left = mid + 1
            else:                      
                right = mid - 1
    
    # Normal BS
    def binary_search(self, nums: List[int], target: int, left, right) -> int:
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                right = mid - 1

            else:
                left = mid + 1

        return -1