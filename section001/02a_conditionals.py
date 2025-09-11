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

