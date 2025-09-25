# 04a - Functions

def say_hello() -> None: # type hint (optional)
    print('Hello')
    return # optional

def get_answer() -> int:
    # print(42) # not to be confused with console output!
    return 42

print(f'{get_answer() * 2 = }')

exec_count: int = 0 # global variable
def power(base: int, exponent: int) -> int:
    '''
    calculates base ^ exponent using repeated multiplication
    returns base ^ exponent
    '''
    result: int = 1 # local variable
    for i in range(exponent):
        result *= base

    global exec_count # bad idea - sloppy code
    exec_count += 1
    print(f'{exec_count = }')

    return result 

print(f'{power(2, 8) = }')
print(f'{power(2, 10) = }')
max_size: int = power(2, 10)

def variable_modifier(val: int, vals: list[int]) -> None:
    val += 1
    vals[0] += 1

num: int = 5
nums: list[int] = [1,2,3,4,5]
variable_modifier(val = num, vals = nums) # named args
print(f'{num = }')
print(f'{nums = }')

print('CSCI', '1030U', sep='', end='')

def calculate_interest(principal=1000, interest_rate=0.035):
   return principal * interest_rate

print(f'{calculate_interest() = }')
print(f'{calculate_interest(principal=5000) = }')
print(f'{calculate_interest(interest_rate=0.045) = }')
print(f'{calculate_interest(principal=2500, interest_rate=0.045) = }')

# coding exercise 04a.1
def get_class_average(marks: list[float]) -> float:
    total: float = 0.0
    for mark in marks:
        total += mark 
    return total / len(marks)

midterm_marks: list[float] = [57.0, 62.5, 68.0, 74.0, 55.0, 71.0, 94.5, 47.5]
midterm_average: float = get_class_average(midterm_marks)
print(f'{midterm_average = }') # 66.1875
