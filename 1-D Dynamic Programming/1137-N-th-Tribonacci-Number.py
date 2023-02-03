class Solution:
    def tribonacci(self, n: int) -> int:
        n1, n2, n3 = 0, 1, 1

        for i in range(n-2):
            s = n1 + n2 + n3
            n1, n2, n3 = n2, n3, s 
        
        return n3 if n > 0 else 0