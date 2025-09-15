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