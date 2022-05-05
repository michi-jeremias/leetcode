"""
https://leetcode.com/problems/implement-stack-using-queues/
"""


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        res = self.stack[-1]
        self.stack = self.stack[:-1]
        return res

    def top(self) -> int:
        res = None
        if not self.empty():
            res = self.stack[-1]
        return res

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
