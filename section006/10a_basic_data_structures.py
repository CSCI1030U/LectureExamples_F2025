# 10a - Basic Data Structures

class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, new_element):
        self.elements.append(new_element)
    
    def top(self):
        if len(self.elements) == 0:
            raise EmptyStackError('Cannot pop from an empty stack')

        return self.elements[-1]
    
    def pop(self):
        if len(self.elements) == 0:
            raise EmptyStackError('Cannot pop from an empty stack')

        return self.elements.pop()
    
    def is_empty(self):
        return len(self.elements) == 0

stack = Stack()
print(f'{stack.is_empty() = }')
stack.push('AAA')
stack.push('BBB')
stack.push('CCC')
print(f'{stack.is_empty() = }')
print(f'{stack.top() = }')
print(f'{stack.pop() = }')
stack.push('DDD')
stack.push('EEE')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
print(f'{stack.pop() = }')
