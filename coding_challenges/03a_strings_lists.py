# Coding Challenge 03a.1

nums =[3, 4, 9, -2, -1, 0, 20, 14, 7, 9, 12]
total = 0
count = 0
for num in nums:
    if num % 2 == 0:
        total += num 
        count += 1
print(f'{total / count = }')

