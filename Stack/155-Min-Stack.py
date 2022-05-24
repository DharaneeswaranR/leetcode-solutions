class MinStack:
    class Node:
        def __init__(self, val, next, Min):
            self.val = val
            self.next = next
            self.Min = Min

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if not self.head:
            self.head = self.Node(val, None, val)
        else:
            self.head = self.Node(val, self.head, min(self.head.Min, val))       

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.Min

"""
Implemented stack using linked list, every node of list holds the minimum element
upto to that node

"""