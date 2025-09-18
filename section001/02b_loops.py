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
for n in range(0, 25):
    top = x ** n 
    bottom = math.factorial(n)
    estimate = estimate + top / bottom 

print(f"estimate of euler's function: {estimate}")

# coding exercise 02b.2
x = 13.0
epsilon = 0.0000001
estimate = x / 2
while abs(estimate ** 2 - x) > epsilon:
    # how much to change?
    change = abs(estimate ** 2 - x) / 8

    # should we add or subtract?
    if (estimate ** 2 - x) < 0:
        estimate += change 
    elif (estimate ** 2 - x) > 0:
        estimate -= change 
    
    print(f'{estimate=}')
print(f'estimate for sqrt({x}) = {estimate}')
print(f'actual sqrt = {math.sqrt(x)}')

