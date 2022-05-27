class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([])
        oper = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in oper:
                a = stack.pop()
                b = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(b / a)) # Truncates to zero 
                    
            else:
                stack.append(int(token))
                
        return stack.pop()