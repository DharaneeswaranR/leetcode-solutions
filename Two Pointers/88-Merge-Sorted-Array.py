# Space - O(n)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = [0] * (m + n)
        i = j = k = 0

        while i < m or j < n:
            if i == m:
                res[k] = nums2[j]
                j += 1
            elif j == n:
                res[k] = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                res[k] = nums1[i]
                i += 1
            else:
                res[k] = nums2[j]
                j += 1
            k += 1

        for i in range(m+n):
            nums1[i] = res[i]

# Space - O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

"""
Approach:

1. Initial (Space - O(n))
   Create a new array of length m+n and use two pointer approach to merge the two arrays
   and copy the new array to nums1

2. Constant space
   The trick is to start from backwards by placing the larger elements from back of nums1
   so it wont mess up nums1 array elements hence eleminating the need for new array
    
"""
        