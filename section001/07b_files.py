# 07b - File Input/Output

# input_file = open('section001/data/fakedata.txt', 'r')
# ... read the file ...
# input_file.close()

with open('section001/data/fakedata.txt', 'r') as input_file:
    print(f'{input_file.read() = }')

import json 

with open('section001/data/products.json', 'r') as products_in:
    products = json.load(products_in)
print(f'{products[0]["price"] = }')

with open('section001/data/customer.json', 'w') as customer_out:
    cust = {
        'first name': 'Adbul',
        'last name': 'Karam',
        'balance': 134.61
    }
    json.dump(cust, customer_out)

# exercise 08a.1

sids = ['100000000', '100000001', '100000002', '100000003', '100000004', '100000005', '100000006', '100000007', '100000008', '100000009']
midterm_marks = [52.0, 48.5, 54.25, 61.5, 64.0, 77.75, 29.0, 91.25, 68.25, 59.75]

with open('section001/data/grades.csv', 'w') as grades_out:
    for i in range(len(sids)):
        grades_out.write(f'{sids[i]}, {midterm_marks[i]}\n')

with open('section001/data/grades.csv', 'r') as grades_in:
    grades = grades_in.readlines()
    for line in grades:
        data = line.split(',')
        sid = int(data[0])
        grade = float(data[1])
        # data[1].strip() - removes extra spacing chars
        print(f'{sid}: {grade}')