class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        _min = 999999
        n = len(nums)
        prefix = [n for n in nums]
        index = 0

        for i in range(1, n):
            prefix[i] += prefix[i - 1]  # Prefix sum array

        for i in range(n):
            if i == n - 1:
                diff = prefix[i] // (i+1)
            else:
                diff = abs((prefix[i] // (i+1)) - ((prefix[-1] - prefix[i]) // (n - i - 1)))
            if diff < _min:
                index = i
                _min = diff

        return index


"""
Soln: Create a prefix sum array

"""
                
                
            