class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = 0
        temp = n
        res = 0
        
        while temp != 0:
            temp //= 10
            digits += 1
            
        flag = True if digits % 2 == 0 else False
        
        while n != 0:
            if flag:
                res -= (n % 10)
                flag = False
            else:
                res += (n % 10)
                flag = True
            n //= 10
            
        return res


"""
Approach: 

Flip the flag boolean every iteration to alternate

"""