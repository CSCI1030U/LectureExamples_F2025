# coding challenge 02b.1
import math

# solution 1 (numbers 1,3,5,..., +/- alternating manually)
x = 3.0 * math.pi / 2.0
estimate = 0.0
adding = True
for n in range(1, 100, 2):
    term = x ** n  / math.factorial(n)
    if adding:
        estimate += term 
    else:
        estimate -= term
    adding = not adding 

print(f"estimate of sin({x}): {estimate}")

# solution 2 (numbers 0,1,2,3,..., +/- with exponents)
x = 3.0 * math.pi / 2.0
estimate = 0.0
adding = True
for n in range(0, 50):
    sign = (-1) ** n
    exponent = x ** (2 * n + 1)
    fact = math.factorial(2 * n + 1)
    estimate += sign * exponent / fact 

print(f"estimate of sin({x}): {estimate}")
