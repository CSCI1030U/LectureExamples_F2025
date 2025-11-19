# 09a - Algorithms

'''
INSERT-SORT(A)
1  for j = 2 to length[A] do
2     key = A[j]
3     i = j-1
4     while i > 0 and A[i] > key do
5        A[i+1] = A[i]
6        i = i-1
7     A[i+1] = key
'''
def insert_sort(elements):
    for j in range(1, len(elements)):
        key = elements[j]
        i = j - 1
        while i >= 0 and elements[i] > key:
            elements[i + 1] = elements[i]
            i -= 1
        elements[i + 1] = key

values = [5, -1, 10, 21, 3, -7, -18, 0, 4, -2]
insert_sort(values)
print(f'{values = }')

# coding exercise 09a.1
def insert_sort_mirror(elements):
    for j in range(len(elements) - 2, -1, -1):
        key = elements[j]
        i = j + 1
        while i <= (len(elements) - 1) and elements[i] < key:
            elements[i - 1] = elements[i]
            i += 1
        elements[i - 1] = key

values = [5, -1, 10, 21, 3, -7, -18, 0, 4, -2]
insert_sort_mirror(values)
print(f'{values = }')

# coding exercise 09a.2
def sequential_search(values, to_find):
    num_ops = 0
    for i in range(len(values)):
        num_ops += 1
        if values[i] == to_find:
            return True, num_ops
    return False, num_ops

list10 = range(10)
list100 = range(100)
list1000 = range(1000)
list10000 = range(10000)
lists = [list10, list100, list1000, list10000]
for current_list in lists:
    result, num_operations = sequential_search(current_list, -1)
    print(f'{len(current_list)}:{num_operations}')