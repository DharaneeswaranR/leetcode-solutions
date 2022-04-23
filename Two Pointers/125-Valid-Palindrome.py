class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l <= r:
            while l < r and not self.isalnum(s[l]):
                l += 1
            while l < r and not self.isalnum(s[r]):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
            
        return True
            
    def isalnum(self, char):
        return (90 >= ord(char) >= 65) or (122 >= ord(char) >= 97) or (57 >= ord(char) >= 48)


"""
Approach:

Two pointers - l, r
Skip non-alphanumeric character using while loop and ignore case and check if char pointed by
left and right pointer is equal.

"""