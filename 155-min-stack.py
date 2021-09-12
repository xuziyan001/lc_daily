class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min = None

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.min is None:
            self.min = val
        else:
            self.min = min(val, self.min)

    def pop(self) -> None:
        if not self.s:
            return
        tmp = self.s.pop(-1)
        if tmp == self.min:
            self.min = None if not self.s else min(self.s)

    def top(self) -> int:
        if not self.s:
            return -1
        return self.s[-1]

    def getMin(self) -> int:
        return self.min


if __name__ == '__main__':
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    s.pop()
    print(s.top())
    print(s.getMin())

# ["MinStack","push","push","push",
# "top","pop","getMin","pop","getMin","pop",
# "push","top","getMin","push","top",
# "getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],
# [],[],[],[],[],[],
# [2147483647],[],[],[-2147483648],[],
# [],[],[]]