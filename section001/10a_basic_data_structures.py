# 10a - Basic Data Structures

class Stack:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, new_element):
        self.elements.append(new_element)

    def pop(self):
        return self.elements.pop()

    def top(self):
        return self.elements[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
