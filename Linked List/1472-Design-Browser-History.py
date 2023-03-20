class DLL:
    def __init__(self, url):
        self.url = url
        self.next = self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = DLL(homepage)
        self.curr = self.head
        
    def visit(self, url: str) -> None:
        self.curr.next = DLL(url)
        temp = self.curr
        self.curr = self.curr.next
        self.curr.prev = temp
        
    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url