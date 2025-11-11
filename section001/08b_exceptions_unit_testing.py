# 08b - Exceptions and Unit Testing

names = ['Bob', 'Lucy', 'Sandra']
# print(f'{names[5] = }')

# int sqrt(int num) {
#     // calculate the square root 

#     if (error) {
#         return -1;
#     }
# }

# coding exercise 08b.1
nums = [5,4,3,2,1,0]
for num in nums:
    try:
        print(f'{1 / num = }')
    except ZeroDivisionError as error:
        print(f'Error while dividing by n: {error}')

class LoginIncorrectError(Exception):
    pass 

username = 'bsmith'
password = 'password'
if username == 'bsmith' and password == 'openup':
    print('Access granted')
else:
    raise LoginIncorrectError('Invalid login credentials')

