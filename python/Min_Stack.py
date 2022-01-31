class MinStack:

    def __init__(self):
        self.items = []
        self.minItem = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if self.minItem:
            val = min(val, self.minItem[-1])
        self.minItem.append(val)

    def pop(self) -> None:
        self.items.pop()
        self.minItem.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minItem[-1]
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
