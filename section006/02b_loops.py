# 02b - Loops

n = 1
while n <= 5:
    print(n)
    n = n + 1 # n += 1
    # without the line above, infinite loop

for x in range(5):
    print(f'{x = }')

for y in range(1, 15, 3):
    print(f'{y = }')

for z in range(20, 10, -1):
    print(f'{z = }')

# while 'False': # weird infinite loop condition (everything but 0 is True)
#     print('Hello')

x = 0
while True:
    if x == 19:
        break # bad code smell
    x += 1


# coding exercise 02b.1
import math 

x = 1
estimate = 0.0
for n in range(0, 2000):
    top = x ** n 
    bottom = math.factorial(n)
    estimate = estimate + (top / bottom)

print(f'{estimate = }')
print(f'{math.exp(1) = }')

# coding exercise 02b.2 (hard mode)
x = 11
estimate = x/2
epsilon = 0.00001
while abs(estimate ** 2 - x) > epsilon:
    adjustment = abs(estimate ** 2 - x) / 4
    if (estimate ** 2 - x) < 0:
        # our estimate is too big
        estimate += adjustment
    else:
        # our estimate is too small
        estimate -= adjustment
print(f'{estimate = }')
print(f'{math.sqrt(x) = }')

# optional homework problem
max = 1000
total = 0
for i in range(1, max):
    if (i % 3) == 0 or (i % 5) == 0:
        # print(f'{i = }')
        total += i 
print(f'The sum of multiples of 3 & 5: {total}')

# for i in range(100000000000):
#     pass 