class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        maximum = nums[0]

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            maximum = max(maximum, curr_sum)
        
        return maximum


"""
Approach: Greedy and DP

Kadane's Algorithm can be viewed both as greedy and DP. As we can see that we are keeping a 
running sum of integers and when it becomes less than 0, we reset it to 0 (Greedy Part). 
This is because continuing with a negative sum is way worse than restarting with a new range.
Now it can also be viewed as a DP, at each stage we have 2 choices: Either take the current 
element and continue with the previous sum OR restart a new range. Both choices are being 
taken care of in the implementation

Source: GeeksforGeeks

"""