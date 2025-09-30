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

# higher-order functions
from typing import Callable 

def traverse(elements: list[float], op: Callable) -> None:
    for item in elements:
        op(item)

def print_if_a(mark: float) -> None:
    if mark >= 80.0:
        print(f'{mark} is an A')

traverse([67.0, 74.5, 90.0, 37.25, 48.0, 84.5, 58.25], print_if_a)

# map()

def get_letter_grade(mark: float) -> str:
    if mark >= 80.0:
        return 'A'
    elif mark >= 70.0:
        return 'B'
    elif mark >= 60.0:
        return 'C'
    elif mark >= 50.0:
        return 'D'
    else:
        return 'F'
    
marks = [67.0, 74.5, 90.0, 37.25, 48.0, 84.5, 58.25]
letter_grades = map(get_letter_grade, marks)
print(f'{list(letter_grades) = }')

# generator example
# for i in (n ** 2 for n in range(50000000000000000000000000000000)):
#     print(i)

scaled_down_marks = map(lambda a: a / 10.0, marks)
print(f'{list(scaled_down_marks) = }')

scale_down = lambda a: a / 10.0
new_mark = scale_down(67.0)
print(f'{new_mark = }')

# calling a lambda function directly
new_mark = (lambda a: a / 10.0)(67.0)
print(f'{new_mark = }')

# reduce()

from functools import reduce

def min2(a: float, b: float) -> float:
    if a < b:
        return a
    else:
        return b
    # return a if a < b else b

marks = [67.0, 74.5, 90.0, 37.25, 48.0, 84.5, 58.25]
minimum_mark = reduce(min2, marks)
print(f'{minimum_mark = }')

maximum_mark = reduce(lambda a, b: a if a > b else b, marks)
print(f'{maximum_mark = }')

# coding exercise 04b.1

invoice_items = [
    {'item_price': 19.99, 'quantity': 3},
    {'item_price': 9.99, 'quantity': 10},
    {'item_price': 4.99, 'quantity': 50},
    {'item_price': 99.99, 'quantity': 1}
]

def get_item_price(invoice_item):
    return invoice_item['item_price'] * invoice_item['quantity']

item_totals = map(get_item_price, invoice_items)

def add2(price1, price2):
    return price1 + price2

total = reduce(add2, item_totals)
print(f'{total = }')