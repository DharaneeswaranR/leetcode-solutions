class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        hashset = set()
        
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        for n in freq.values():
            if n in hashset:
                return False
            hashset.add(n)
            
        return True

"""
Find freq using hashmap and check for repeating value using hashset

"""