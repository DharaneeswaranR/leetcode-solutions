class Solution:
    def solve(self, n, p, op, cl, res):
        if cl == n:
            res.append(p)
            return
        if op < n: # If no. of open brackets is less than n add open bracket
            self.solve(n, p + "(", op + 1, cl, res)
        if op > cl: # close bracket can be added only if open > close
            self.solve(n, p + ")", op, cl + 1, res)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.solve(n, "", 0, 0, res)
        return res
    
