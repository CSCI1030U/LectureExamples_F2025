# 09a - Algorithms

# coding exercise 09a.1
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
def insert_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

grades = [91.0, 45.5, 65.25, 71.5, 32.0, 84.5, 71.0, 55.25]
insert_sort(grades)
print(f'{grades = }')

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
for input_list in lists:
    result, num_ops = sequential_search(input_list, -1)
    print(f'{len(input_list)}:{num_ops}')
