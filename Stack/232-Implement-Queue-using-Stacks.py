class MyQueue:
    def __init__(self):
        self.stackPush = deque()
        self.stackPop = deque()

    def push(self, x: int) -> None:
        self.stackPush.append(x)            

    def pop(self) -> int:
        self.peek()
        return self.stackPop.pop()

    def peek(self) -> int: 
        if len(self.stackPop) == 0:
            while self.stackPush:
                self.stackPop.append(self.stackPush.pop())
        
        return self.stackPop[- 1]

    def empty(self) -> bool:
        return not len(self.stackPush) and not len(self.stackPop)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
Approach:

Push the contents of stack to new stack so the top element will be the first element. Only push all the 
elements from stack to new stack if all the elements from the new stack is popped out ie empty.

"""