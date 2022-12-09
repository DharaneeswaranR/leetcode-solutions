class Solution:
    def myAtoi(self, s: str) -> int:
        num_read = False
        sign_read = False
        pzero_read = False
        is_neg = False
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        num = 0
        for char in s:
            if not self.is_num(char) and not num_read:
                if char == ' ' and not sign_read and not pzero_read:
                    continue
                elif char == '-' and not sign_read and not pzero_read:
                    is_neg = True
                    sign_read = True
                elif char == '+' and not sign_read:
                    is_neg = False
                    sign_read = True
                else:
                    break
            if not self.is_num(char) and num_read:
                break
            if self.is_num(char):
                if char == '0' and not num_read:
                    pzero_read = True
                    continue
                num = num * 10 + int(char)
                num_read = True
        
        num = -1 * num if is_neg else num

        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        return num     
    
    def is_num(self, char):
        return 48 <= ord(char) <= 57
        

"""
Approach:

It's is mess, I know.

"""