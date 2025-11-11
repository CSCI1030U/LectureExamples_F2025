# 08b - Exceptions and Unit Testing

names = ['bob', 'sandra', 'lucy']
# print(f'{names[5] = }')

# warning: do not hide runtime errors!
try:
    with open('fakefile.txt', 'r') as f:
        contents = f.read()
except FileNotFoundError as error:
    print(error)
except Exception as error: # all errors
    print(error)

# print(contents)

class LoginIncorrectError(Exception):
    pass 

email = 'bsmith@gmail.com'
password = 'wrong'
if email == 'bsmith@gmail.com' and password == 'openup':
    print('Access granted')
else:
    raise LoginIncorrectError('Invalid email or password')


'''
float sqrt(float val) {
    ...
    if (valid root) {
        return root;
    } else {
        return -1; // ambiguous and ancient
    }
}
'''