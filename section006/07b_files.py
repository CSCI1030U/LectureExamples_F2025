# 07b - File Input/Output

# input_file = open('section006/data/plaintext.txt', 'r')
# ...
# input_file.close()

with open('section006/data/plaintext.txt', 'r') as input_file:
    contents = input_file.readlines()
    print(f'{contents = }')

with open('section006/data/output.txt', 'w') as out_file:
    out_file.write('This is the first line.\n')
    out_file.write('This is the second line.')

import json
with open('section006/data/carla.json', 'r') as json_input:
    carla = json.load(json_input)
    print(f'{carla = }')