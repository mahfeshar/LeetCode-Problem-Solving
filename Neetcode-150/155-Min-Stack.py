class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = float('inf')

    def push(self, val: int) -> None:
        self.min_num = min(self.min_num, val)
        self.stack.append(val)

    def pop(self) -> None:
        poped = self.stack.pop()
        if poped == self.min_num:
            self.min_num = min(self.stack, default=float('inf'))

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# -2 0 -3 