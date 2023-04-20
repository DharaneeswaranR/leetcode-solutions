class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left < right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        
        return left - 1 if not left <= 1 else left

"""
Approach:

- The idea is to use binary search to find the square root of the number.
- The left and right variables are initialized to 0 and x respectively as the sqrt must be between 0 and x(solution space).
- We take mid * mid and compare it to x.
- If it is less than or equal to x, we set left to mid + 1.
- If it is greater than x, we set right to mid.
- We repeat this process until left is less than right and we find the sqrt.

"""