class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = 9999
        hashmap = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        for c in text:
            if c in hashmap:
                hashmap[c] += 1
        
        hashmap['l'] //= 2
        hashmap['o'] //= 2

        for count in hashmap.values():
            res = min(count, res)

        return res