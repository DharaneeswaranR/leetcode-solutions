class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

  
"""
Approach: Two pointers

- Set two pointers at start and end of the array as we need maximum width
- Move the pointer which has less height to next height 
- Track the area at each step

"""
            