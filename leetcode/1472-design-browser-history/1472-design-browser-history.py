class Node:
    def __init__(self, url):
        self.val = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        new_Node = Node(url)

        self.curr.next = new_Node
        new_Node.prev = self.curr
        self.curr = new_Node

    def back(self, steps: int) -> str:

        while self.curr.prev and steps:
            self.curr = self.curr.prev

            steps -= 1

        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps:
            self.curr = self.curr.next

            steps -= 1

        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)