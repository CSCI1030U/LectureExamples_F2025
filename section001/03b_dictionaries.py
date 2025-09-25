# coding exercise 03b.1

sentence = 'ahmed runs quickly'
words = []
current_word = ''
for letter in sentence:
    if letter == ' ':
        words.insert(0, current_word)
        current_word = ''
    else:
        current_word += letter 
words.insert(0, current_word)

print(f'{words = }')

reverse_sentence = ''
for word in words:
    reverse_sentence += word + ' '
print(f'{reverse_sentence = }')

words = 'ahmed runs quickly'.split(' ')
reverse_words = words[::-1]
reverse_sentence = ' '.join(reverse_words)
print(f'{reverse_sentence = }')

# dictionaries

carla = {
    'sid': 100000001,
    'first name': 'Carla',
    'last_name': 'Rodriguez',
    'midterm_mark': 74.25
}
print(f'{carla["midterm_mark"] = }')

# for key in carla:
#     print(f'{key = }')

for key in carla.keys():
    print(f'{key = }, {carla[key] = }')
print(f'{carla = }')

# coding exercise 03b.2

email = '''Dear sir or madam Your awesome recent purchase of 1000 awesome tiny dog figurines to the awesome amount of $8325 is being processed We hope that you will enjoy your purchase If this order is an error please contact us at totallynotascam@amazon.com The Orders Department'''

# 1. divide the paragraph into words
words = email.split(' ')
print(f'{words = }')

# 2. for each word, update the frequency dictionary
frequencies = {}
for word in words:
    # if the word is not in frequency dictionary, add it with value = 1
    # if the word is in the dictionary, increment the count by 1
    if word.lower() in frequencies:
        frequencies[word.lower()] += 1
    else:
        frequencies[word.lower()] = 1
print(f'{frequencies = }')
