class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {} # char -> freq
        
        for x in s:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
            
        for y in t:
            if y not in hashmap:
                return False
            hashmap[y] -= 1
                
        for i in hashmap.values():
            if i != 0:
                return False
        
        return True
        

"""
Approach:

For two string to be anagram, the strings must follow two conditions
1. Should be of same length
2. Frequency of every character should be same

First condition can be checked with a if condition and the second conditon
can be checked using hashmap by storing char as keys and its freq as values.

"""