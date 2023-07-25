class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, (n - 1) // 2)
        
    
"""
Approach: Binary exponentiation

For example,

2 ^ 100 will have 100 steps (recursive calls)
we could reduce the number of steps by using binary exponentiation

2 ^ 100 = (2 * 2)^50
4 ^ 50 = (4 * 4)^25
16 ^ 25 = 16 * (16)^24 = 16 * (16 * 16)^12

So if n is even, then return myPow(x * x, n // 2)
else if n is odd, then return x * myPow(x * x, (n - 1) // 2)

"""