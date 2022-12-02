class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        h = len(s) // 2
        c1 = c2 = 0
        
        for c in s[0:h]:
            if self.isVowel(c):
                c1 += 1
                
        for c in s[h:]:
            if self.isVowel(c):
                c2 += 1
                
        return c1 == c2
    
    def isVowel(self, char):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        return char in vowels
        
