# 03a - Strings and Lists

# coding exercise 03a.1
full_name = 'Keanu Reaves'
first_name = ''
last_name = ''
first = True 
for letter in full_name:
    if letter == ' ':
        first = False 
    elif first:
        first_name += letter 
    else:
        last_name += letter
print(f'{first_name = }')
print(f'{last_name = }')

full_name = 'Barack Obama'
space_index = full_name.index(' ')
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]
print(f'{first_name = }')
print(f'{last_name = }')

nums = [2,4,6,8,10,4,6,8]
nums.remove(4)
print(f'{nums = }')

# print(f'{sum(["One", "Two", "Three"]) = }')

matrix = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
print(f'{matrix[1][0] = }')

# coding exercise 03a.2

midterm_marks: list[float] = [41.0, 65.0, 72.5, 74.25, 55.0, 61.0, 84.5]

# add up all the marks (find the sum)
total = 0.0
count = 0
for mark in midterm_marks:
    total += mark
    count += 1

# divide by the number of marks
print(f'{total / count = }')
print(f'{sum(midterm_marks) / len(midterm_marks) = }')