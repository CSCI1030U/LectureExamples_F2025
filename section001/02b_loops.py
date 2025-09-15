# 02b - Loops

n = 0
while n < 10:
    print(f'{n} is a single-digit number.')
    # n += 1
    n = n + 1

for n in [2,4,9]:
    print(f'List element: {n}')

for n in range(15, 5, 1):
    print(f'Range element: {n}')

n = 0
while n <= 5:
    # if n > 5:
    #     break
    print('Hello')
    n += 1

# coding exercise 02b.1
import math
# from math import factorial
x = 1
estimate = 0.0
for n in range(0, 25000000):
    top = x ** n 
    bottom = math.factorial(n)
    estimate = estimate + top / bottom 

print(f"estimate of euler's function: {estimate}")
