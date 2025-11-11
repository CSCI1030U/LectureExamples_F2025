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

with open('section006/data/products.json', 'w') as products_out:
    products = [
        {
            'product_id': 1,
            'name': '102 Key Keyboard',
            'price': 29.99
        },
        {
            'product_id': 2,
            'name': 'i7 13600h',
            'price': 249.99
        }
    ]
    json.dump(products, products_out)

# coding exercise 07b.1
sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]

with open('section006/data/grade_output.csv', 'w') as grade_output:
    for i in range(len(sids)):
        grade_output.write(f'{sids[i]}, {midterm_marks[i]}\n')

# coding exercise 07b.2
marks = []
with open('section006/data/grade_output.csv', 'r') as grades_in:
    lines = grades_in.readlines()
    for line in lines:
        data = line.split(',')
        sid = int(data[0])
        mark = float(data[1])
        print(f'{data[1].strip() = }') # how to strip spacing
        student = {
            'sid': sid,
            'midterm_mark': mark
        }
        marks.append(student)
print(f'{marks = }')
print(f'{marks[1] = }')
print(f'{marks[1]["midterm_mark"] = }')