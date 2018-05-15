class Stack:

    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0


def stack_to_queue(stack_1, stack_2):
    if not stack_1.is_empty():
        while stack_1.size() > 0:
            stack_2.push(stack_1.pop())
        queue = stack_2.pop()
        while stack_2.size() > 0:
            stack_1.push(stack_2.pop())
        return queue


if __name__ == "main":
    stack_1 = Stack()
    stack_2 = Stack()
    stack_1.push(1)
    stack_1.push(2)
    stack_1.push(3)
    stack_1.push(5)
    stack_1.push(6)
    stack_to_queue(stack_1, stack_2)
