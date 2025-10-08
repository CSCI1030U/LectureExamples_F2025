# 05a - Recursion

def forever(message):
    print(message)
    forever(message)

# forever('hello') # infinite recursion

def repeat_n_times(n, message):
    if n < 1:
        return
    
    print(f'repeat_n_times: {n = } {message = }')

    repeat_n_times(n - 1, message)

    # will happen in reverse order
    # print(f'repeat_n_times: {n = } {message = }')

repeat_n_times(3, 'Hello!')

# coding exercise 1

# 0, 1, 1, 2, 3, 5, 8, 13, ...

def fib(n):
    if n <= 1:
        return n 
    
    return fib(n - 1) + fib(n - 2)

print(f'{fib(2) = }')
print(f'{fib(5) = }')
print(f'{fib(8) = }')
# print(f'{fib(50) = }') # heat death of the universe

# practice problem #3

def is_reverse(str1: str, str2: str) -> bool:
    # 1. base case
    if len(str1) == 0 and len(str2) == 0:
        return True

    if len(str1) == 1 and len(str2) == 1:
        # if str1[0] == str2[0]:
        #     return True 
        # else:
        #     return False
        return str1[0] == str2[0]

    # 2. recursive case
    # a. check if they one character that matches
    # b. check if the rest of the two strings are reverse of one another
    if str1[0] != str2[-1]:
        return False
    else:
        # print(f'is_reverse({str1}, {str2})')
        # print(f' {str1[1:] = }')
        # print(f' {str2[0:-1] = }')
        return is_reverse(str1[1:], str2[0:-1])

print(f'{is_reverse("abcd", "dcba") = }')
print(f'{is_reverse("abcd", "cdba") = }')
print(f'{is_reverse("abcd", "abcd") = }')
print(f'{is_reverse("a", "a") = }')
print(f'{is_reverse("", "") = }')
