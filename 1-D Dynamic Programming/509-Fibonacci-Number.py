class Solution:
    def fib(self, n: int) -> int:
        n1, n2 = 0, 1

        for _ in range(n-1):
            s = n1 + n2
            n1, n2 = n2, s

        return n2 if n > 0 else n

