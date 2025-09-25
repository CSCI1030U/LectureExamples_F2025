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