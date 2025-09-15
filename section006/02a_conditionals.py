# 02a - Conditionals

age = 17
if age >= 19:
    print('Have fun in the club!')
    print('Be safe!')

print('Goodbye!')

final_mark = 54
if final_mark < 50:
    print('F')
elif final_mark < 60:
    print('D')
elif final_mark < 70:
    print('C')
elif final_mark < 80:
    print('B')
else:
    print('A')

# coding exercise 02a.1
a = int(input('Enter A: '))
b = int(input('Enter B: '))
if (a % 2) == 0 and (b % 2) == 0:
    print('Both numbers are even.')

# coding exercise 02a.2
health_points = 3
if health_points <= 0:
    is_dead = True 
else:
    is_dead = False 

