# 03a - Strings and Lists

customer_name = 'Barbara'
spam = f'''
Dear {customer_name},

Buy more of our stuff.  We're broke.

Sincerely
The Company
'''

multiline = 'line 1\nline 2'

print(f'{spam[2:20:3] = }')
print(f'{spam[::-1] = }')
print(f'{len(spam) = }')

for c in multiline:
    print(f'{c = }')

# coding exercise 03a.1
full_name = 'Ahmed Abdullah'
first_name = ''
last_name = ''
for index in range(len(full_name)):
    if full_name[index] == ' ':
        space_index = index 
first_name = full_name[0:space_index]
last_name = full_name[space_index + 1:]
print(f'{first_name = }')
print(f'{last_name = }')

# using the built-in function
first_name,last_name = full_name.split(" ")
print(f'{first_name = }')
print(f'{last_name = }')

nums = [0,2,4,6,8]
nums.insert(-1, 7)
nums.insert(5, 10)
nums.append(11)
print(f'{nums = }')
nums.remove(8)
print(f'{nums = }')
nums.pop()
print(f'{nums = }')
nums.pop(0)
print(f'{nums = }')

names: list[str] = ['Bill', 'Dani', 'Carla', 'Gale']
# print(sum(names))

matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
print(f'{matrix[2][1] = }')

# coding exercise 03a.2
marks = [57.5, 72.0, 91.25, 100.0, 44.0, 65.5, 75.25]
# 1. add the marks together
total = 0.0
for mark in marks:
    total += mark 
# 2. divide by the number of marks
print(f'{total / len(marks) = }')