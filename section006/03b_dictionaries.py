# 03b - Dictionaries

carla = {
    'sid': 100000001,
    'first_name': 'Carla',
    'last_name': "Rogriguez",
    'quiz_mark': 8.0,
    'midterm_mark': 74.5
}

print(f'{carla["midterm_mark"] = }')

for key in carla.keys():
    print(f'{key = }, {carla[key] = }')
print(f'{carla = }')

# coding exercise 03b.2

paragraph = '''Dear sir or madam, Your recent order for a thousand dollars worth of plastic goose figurines is being processed  Message us if this order is in error with your credit card # and your mother's maiden name The orders processing department'''
words = paragraph.split(' ')
frequency = {}
for word in words:
    if word in frequency:
        print(f'found {word = }')
        frequency[word] += 1
    else:
        print(f'not found {word = }')
        frequency[word] = 1
print(f'{frequency = }')
