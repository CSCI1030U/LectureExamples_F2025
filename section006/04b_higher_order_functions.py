# 04b - Higher Order Functions

def a(message) -> None:
    print(f'a:{message}')

def b(message) -> None:
    a(message)
    print(f'b:{message}')

def c(message) -> None:
    b(message)
    print(f'c:{message}')

c('hello')