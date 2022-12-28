class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        map1, map2 = {}, {}
        i = 0
        
        for c in pattern:
            if c in map1 and map1[c] != s[i]:
                return False
            if s[i] in map2 and map2[s[i]] != c:
                return False
            map1[c] = s[i]
            map2[s[i]] = c
            i += 1

        return True

"""
Approach: Hashmap 

Similar to 205-Isomrphic-Strings

"""