class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set("aeiou")
        count = 0

        for i in range(k):
            if s[i] in vowel:
                count += 1

        max_count = count
        i, j = 1, k
        while j < len(s):
            if s[i-1] not in vowel and s[j] in vowel:
                count += 1
            elif s[i-1] in vowel and s[j] not in vowel:
                count -= 1
            max_count = max(count, max_count)
            i += 1
            j += 1

        return max_count