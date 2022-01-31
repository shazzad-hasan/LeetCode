class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.insert(0, x)

    def pop(self) -> int:
        return self.items.pop()

    def peek(self) -> int:
        return self.items[len(self.items)-1]

    def empty(self) -> bool:
        return self.items == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()