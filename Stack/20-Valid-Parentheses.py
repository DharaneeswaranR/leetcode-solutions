class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        hashmap = {'(': ')', '{': '}', '[': ']'}
        stack = deque([])
        
        
        for char in s:
            if char in hashmap:
                stack.append(char) # Push all opening parentheses into stack
            else:
                if not stack or char != hashmap[stack.pop()]: # Pop from stack if closing parentheses and check if popped element
                    return False                              # matches 
                
        return not stack 
