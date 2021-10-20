from collections import deque  # Importing Deque


class Stack:                    # Class for Stack Implementation
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


def evaluate(exp):     # Function for evaluating prefix expression
    """
     Note: I am using stack here for reversing the order of expression
     Because I think that it maybe more efficient than traditional ways
     Further knowledge and research is required
    """
    express = Stack()   # Stack for reversing expression
    eva = Stack()       # Stack for storing expression data durning evaluation

    for c in exp:       # Loop for pushing an epression into reversing stack
        express.push(c)

    for x in range(express.size()):  # Loop for evaluation
        popped = express.pop()       # Pop element at a time

        # Check if popped element is operand or not
        if popped.isalpha() or popped in '1234567890': 
            eva.push(popped)

        # Check else if popped element is operator or not
        elif popped in '+-*/':
            op1 = int(eva.pop())
            op2 = int(eva.pop())

            # Following conditions performs arithimetic operations
            # based upon type of character
            if popped == '+':
                eva.push(op2 + op1)
            elif popped == '-':
                eva.push(op2 - op1)
            elif popped == '*':
                eva.push(op2 * op1)
            else:
                eva.push(op2 / op1)
    return eva.top()

# Calling function for evaluation:-
if __name__ == '__main__':
    expression = "+7*45+21"
    print("Prefix Expression Evaluation: ", expression, end="")
    print(" == ", evaluate(expression))
