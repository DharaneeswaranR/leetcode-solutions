class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                l += 1
            else:
                l = 0
            res += l
        return res


"""
Approach:

For an array [0, 0, 0, 0, 0] there are 1 + 2 + 3 + 4 + 5 = 15 subarrays filled 
with 0's. So we consecutively add length of subtrings containing 0's

"""