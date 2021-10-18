from collections import deque


class Stack:
    def __init__(self) -> None:
        self.control = deque()

    def push(self, val):
        self.control.append(val)

    def pop(self):
        if len(self.control) == 0:
            return 0
        else:
            return self.control.pop()

    def top(self):
        if len(self.control) == 0:
            return 0
        else:
            return self.control[-1]

    def size(self):
        return len(self.control)
    
    def is_empty(self):
        return len(self.control) == 0