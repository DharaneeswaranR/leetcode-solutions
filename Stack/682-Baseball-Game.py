class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque([])

        for opr in operations:
            if opr == "C":
                stack.pop()
            elif opr == "D":
                stack.append(stack[-1] * 2)
            elif opr == "+":
                x = stack.pop()
                y = stack[-1]
                stack.append(x)
                stack.append(x + y)
            else:
                stack.append(int(opr))  

        return sum(stack)