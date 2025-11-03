# 07b - File Input/Output

# input_file = open('section001/data/fakedata.txt', 'r')
# ... read the file ...
# input_file.close()

with open('section001/data/fakedata.txt', 'r') as input_file:
    print(f'{input_file.read() = }')
