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
password = 'openup'
if username == 'bsmith' and password == 'openup':
    print('Access granted')
else:
    raise LoginIncorrectError('Invalid login credentials')

# programming exercise 08b.2
class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
        self.marks = []

    def set_mark(self, course, mark):
        self.marks.append(mark)

    def get_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return sum / len(self.marks)

import unittest 

class Student_Test(unittest.TestCase):
    def test_init(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertEqual(clarissa.gpa, 0.0)
        # self.assertAlmostEqual(clarissa.gpa, 0.0, 0.00001)
        self.assertEqual(clarissa.name, 'Clarissa')

    def test_set_mark(self):
        clarissa = Student(0.0, 'Clarissa')
        self.assertEqual(clarissa.marks, [])
        clarissa.set_mark('CSCI1030U', 71.5)
        self.assertEqual(clarissa.marks, [71.5])
        clarissa.set_mark('CSCI1060U', 68.25)
        self.assertEqual(clarissa.marks, [71.5, 68.25])

    def test_get_average(self):
        clarissa = Student(0.0, 'Clarissa')
        clarissa.set_mark('CSCI1030U', 71.0)
        clarissa.set_mark('CSCI1060U', 68.0)
        self.assertAlmostEqual(clarissa.get_average(), 69.5, 0.001)
        

unittest.main()