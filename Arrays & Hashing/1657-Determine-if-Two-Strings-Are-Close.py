class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        freq1 = {}
        freq2 = {}
        
        for i in range(len(word1)):
            if word1[i] in freq1:
                freq1[word1[i]] += 1
            else:
                freq1[word1[i]] = 1
                
            if word2[i] in freq2:
                freq2[word2[i]] += 1
            else:
                freq2[word2[i]] = 1
        
        return set(word1) == set(word2) and sorted(freq1.values()) == sorted(freq2.values())


"""
1. Frequency of Char need's to be same there both of string as we can do Transform every occurrence 
of one existing character into another existing character

2. All the unique char which there in String1 need's to there as well In string2 - we can use hashset

"""