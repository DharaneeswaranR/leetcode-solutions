# Sorting - O(nlogn)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])


# Linear - O(n)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = min2 = 9999
        max1 = max2 = max3 = -9999

        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num
        
        return max(min1 * min2 * max1, max3 * max2 * max1)


"""
Approach:

To max prod of three numbers in array can either be:

1. product of 3 largest number or
2. product of two minimum negative number(gives positive number) and a largest number

"""