class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid - 1] < arr[mid] > arr[mid + 1]:  # mid element is greater than both neighbors so it is the peak index
                return mid
            elif arr[mid] > arr[mid + 1]: # mid element is greater than right element
                right = mid
            else:
                left = mid


"""
Approach: Binary search

- If mid element is greater than both neighbors, it is the peak index
- If mid element is greater than right element, the mid element is in right slope and the peak
  index is in left side
- If mid element is greater than left element, the mid element is in left slope and the peak index
  is in right side
  
"""


