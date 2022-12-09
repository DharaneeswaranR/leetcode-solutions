class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_len = 0 
        l = len(s)
        
        for i in range(-1, -l-1, -1):
            if s[i] == " ":
                if word_len == 0:
                    continue
                else:
                    return word_len
            else:
                word_len += 1

        return word_len