class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i = j = 0
        swap = False
        l1, l2 = len(word1), len(word2)

        while i < l1 or j < l2:
            if i >= l1:
                return merged + word2[j:]
            if j >= l2:
                return merged + word1[i:] 
            if swap:
                merged += word2[j]
                j += 1
                swap = False
            else:
                merged += word1[i]  
                i += 1 
                swap = True         

        return merged