class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)
        
        while left < right:
            Sum = numbers[left] + numbers[right]
            
            if Sum == target:
                return [left + 1, right + 1]
            elif Sum > target:
                right -= 1
            else:
                left += 1

                
"""
Approach:

As the array is sorted ie. smallest number on the leftmost and the largest number
on the rightmost. We create a two pointers, one pointing the largest and the other 
the smallest. Then we add both the smallest and the largest numbers, if sum == target
we return its indices, if sum > target, then we have decrement the right pointer as we 
need a smaller sum, if sum < target, then we have to increment the left pointer as we 
need a larger sum.

Time Complexity: linear

"""