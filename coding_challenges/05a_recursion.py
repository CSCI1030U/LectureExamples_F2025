# Coding Challenge 05a.1

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

print(f'{factorial(150) = }')
