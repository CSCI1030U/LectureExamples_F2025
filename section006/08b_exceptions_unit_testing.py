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
password = 'openup'
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

# programming exercise 08b.1
numbers = [5,4,3,2,1,0]
for num in numbers:
    try:
        print(f'{1 / num = }')
    except ZeroDivisionError as error:
        print(error) # not a good idea to hide the error!

# coding exercise 08b.2

class AverageEmptyListError(Exception):
    pass 

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
        self.marks = []

    def set_mark(self, course, mark):
        self.marks.append(mark)

    def get_average(self):
        if len(self.marks) == 0:
            raise AverageEmptyListError('No marks to compute average')

        sum = 0
        for mark in self.marks:
            sum += mark
        return sum / len(self.marks)

import unittest 

class Student_Test(unittest.TestCase):
    def test_init(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertEqual(clarissa.gpa, 0.0)
        self.assertEqual(clarissa.name, 'Clarissa')
        self.assertEqual(clarissa.marks, [])

    def test_set_mark(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertTrue(len(clarissa.marks) == 0)
        clarissa.set_mark('CSCI1030U', 75.0)
        self.assertEqual(clarissa.marks, [75.0])
        clarissa.set_mark('CSCI1060U', 65.0)
        self.assertEqual(clarissa.marks, [75.0, 65.0])

    def test_get_average(self):
        clarissa = Student(0.0, 'Clarissa')
        # self.assertRaises(AverageEmptyListError, clarissa.get_average())
        clarissa.set_mark('CSCI1030U', 75.0)
        self.assertAlmostEqual(clarissa.get_average(), 75.0, 0.0001)
        clarissa.set_mark('CSCI1060U', 65.0)
        self.assertAlmostEqual(clarissa.get_average(), 70.0, 0.0001)
        
unittest.main()