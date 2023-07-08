class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dial = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []

        def solve(i, n, digits, s):
            if i == n:
                res.append(s)
                return
            
            num = digits[i]
            for j in range(len(dial[num])):
                solve(i + 1, n, digits, s + dial[num][j])

        if digits == "": return []

        n = len(digits)
        solve(0, n, digits, "")

        return res
    
