class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        l= len(word)
        count = 0

        for char in word:
            if 'A' <= char <= 'Z':
                count += 1

        if count == l or count == 0:
            return True
        else:
            return 'A' <= word[0] <= 'Z' and count == 1


"""
Approach: 

The given conditions -

1. All capital - count the number of capital letters and return true if length of string is
   equal to the count

2. All lowecase - return true if count of capital letters is 0

3. First letter capital - return true if first letter is capital and capital count is 1

"""