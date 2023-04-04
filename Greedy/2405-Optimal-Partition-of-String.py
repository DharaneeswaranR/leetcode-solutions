class Solution:
    def partitionString(self, s: str) -> int:
        hashset = set()
        count = 0
        for c in s:
            if c in hashset:
                hashset = {c,}
                count += 1
            else:
                hashset.add(c)
        return count + 1

"""
Approach:

We can consider adding characters to a substring as long as we don't see a character 
that has already been added to the current substring. When we see a character that 
is already present in the substring, we start a new substring and repeat this process 
until we iterate over the entire string.

"""