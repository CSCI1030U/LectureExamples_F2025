# 04a - Functions

def say_hello() -> None:
    print('Hello')

say_hello()
say_hello()

def get_answer() -> int:
    return 42

answer: int = get_answer() * 2
print(f'{answer = }')

def power(base: int, exp: int) -> int:
    product: int = 1
    for i in range(exp):
        product *= base 
    return product 

print(f'{power(2,8) = }')
print(f'{power(2,10) = }')

# not recommended coding style!
call_count = 0

def say_ciao():
    global call_count
    call_count += 1
    print('Ciao!')

say_ciao()
say_ciao()
print(f'{call_count = }')

print('val1', 'val2', sep=',', end='\n\n')

def calculate_interest(principal=1000, interest_rate=0.035):
    return principal * interest_rate

print(f'{calculate_interest() = }')
print(f'{calculate_interest(principal=2500) = }')
print(f'{calculate_interest(interest_rate=0.045) = }')
print(f'{calculate_interest(principal=2500, interest_rate=0.045) = }')

# coding exercise 04a.1
def get_class_average(marks: list[float]) -> float:
    total: float = 0.0
    count: int = 0
    for mark in marks:
        total += mark
        count += 1
    return total / count 

print(f'{get_class_average([57.0, 62.5, 68.0, 74.0, 55.0, 71.0, 94.5, 47.5]) = }')

