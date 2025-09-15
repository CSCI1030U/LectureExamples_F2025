# 02a - Conditionals

age = 7
if age < 8:
    print('You must use the dock')

print('Have fun!')

mario_hp = 2 
if mario_hp < 5:
    print('BEEP BEEP BEEP BEEP')

if mario_hp <= 5:
    print('Exhausted mario')
else:
    print("Regular mario")

mark = 87.5
if mark >= 80.0:
    print('A')
elif mark >= 70.0: # if mark < 80.0 and mark >= 70.0
    print('B')
elif mark >= 60.0:
    print('C')
elif mark >= 50.0:
    print('D')
else:
    print('F')

# coding exercise 02a.1
a = int(input('Enter A:'))
b = int(input('Enter B:'))
if ((a % 2) == 0):
    if ((b % 2) == 0):
        print('Both numbers are even.')

if ((a % 2) == 0) and (b % 2) == 0:
    print('Both numbers are even.')

# coding exercise 02a.2
n = 211
if abs(100 - n) <= 10:
    print(True)
elif abs(200 - n) <= 10:
    print(True)
else:
    print(False)

# coding exercise 02a.3
health_points = 3
if health_points <= 0:
    is_dead = True 
else:
    is_dead = False 
    