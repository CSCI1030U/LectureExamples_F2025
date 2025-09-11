# 01b - Errors

# first_name = 'Randy" # syntax errors
# x + 1 = 1

first_name = 'Randy'
print(first_name[0])
# print(first_name[100]) # runtime error

total = 77
total += 65
total += 92
count = 2 # logic error
print(f'{total = }')
print(f'{count = }')
print(f'average: {total / count = }')

# calculate an average of a list

# sum all of the numbers from the list
# count the numbers in the list
# divide the sum by the count

# coding exercise 01b.1
num1 = int(input('Enter the first number: '))
num2 = int(input("Enter the second number: "))
print(f'The answer is {(num1 + num2 ) % 5}')
