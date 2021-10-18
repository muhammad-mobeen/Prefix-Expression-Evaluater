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


def evaluator(exp):
    express = Stack()
    eva = Stack()
    for c in exp:
        express.push(c)

    for x in range(express.size()):
        popped = express.pop()
        if popped.isalpha() or popped in '1234567890':
            eva.push(popped)
        elif popped in '+-*/':
            op1 = int(eva.pop())
            op2 = int(eva.pop())
            if popped == '+':
                eva.push(op2 + op1)
            elif popped == '-':
                eva.push(op2 - op1)
            elif popped == '*':
                eva.push(op2 * op1)
            else:
                eva.push(op2 / op1)
    return eva.top()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "-+7*45+20"
    print(evaluator(s))
