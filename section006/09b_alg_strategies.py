# 09b - Algorithm Strategies

# coding exercise 09b.1

def dc_search(elements, to_find):
    # base case(s)
    if len(elements) == 0:
        return False 
    elif len(elements) == 1:
        return elements[0] == to_find

    # divide
    middle = len(elements) // 2
    first = elements[:middle]
    second = elements[middle:]

    # conquer
    first_result = dc_search(first, to_find)
    second_result = dc_search(second, to_find)

    # combine
    return first_result or second_result

print(f'{dc_search([4, 8, 1, -3, 9, 8, 3, -1, 10, 5], 3) = }')
print(f'{dc_search([4, 8, 1, -3, 9, 8, 3, -1, 10, 5], -3) = }')
print(f'{dc_search([4, 8, 1, -3, 9, 8, 3, -1, 10, 5], 10) = }')
print(f'{dc_search([4, 8, 1, -3, 9, 8, 3, -1, 10, 5], 4) = }')
print(f'{dc_search([4, 8, 1, -3, 9, 8, 3, -1, 10, 5], 5) = }')
print(f'{dc_search([4, 8, 1, -3, 9, 8, 3, -1, 10, 5], 7) = }')

# coding exercise 09b.2

items = [
    {'name': 'Wooden Sculpture', 'value': 3.5, 'weight': 2.0},
    {'name': 'Silver Earrings', 'value': 150.0, 'weight': 1.0},
    {'name': 'Diamond Necklace', 'value': 750.0, 'weight': 1.0},
    {'name': 'Stone Statue', 'value': 8.5, 'weight': 45.0},
    {'name': 'Gold Bracelet', 'value': 275.0, 'weight': 5.0}
]

def insert_sort(elements):
    for j in range(1, len(elements)):
        key = elements[j]
        i = j - 1
        while i >= 0 and elements[i]['ratio'] < key['ratio']:
            elements[i + 1] = elements[i]
            i -= 1
        elements[i + 1] = key

def fractional_knapsack(available_items, capacity):
    # calculate the value/weight ratio for each item
    for item in available_items:
        item['ratio'] = item['value'] / item['weight']

    # sort the list of items in descending order by value/weight
    insert_sort(available_items)

    # insert items in order into the backpack until backpack is full
    backpack = []
    for item in available_items:
        if item['weight'] <= capacity:
            backpack.append(item)
            capacity -= item['weight']
        else:
            fraction_to_take = capacity / item['weight']
            part_item = {
                'name': item['name'],
                'value': item['value'] * fraction_to_take,
                'weight': item['weight'] * fraction_to_take,
                'ratio': item['ratio']
            }
            backpack.append(part_item)
            return backpack


print(f'{fractional_knapsack(items, 8.5) = }')

# coding exercise 09b.3

def fib_dp(n: int) -> int:
    solutions : list[int] = [0, 1]
    # if n < 2:
    #     return n
    for i in range(2, n + 1):
        solutions.append(solutions[i - 1] + solutions[i - 2])
    return solutions[n]

print(f'{fib_dp(10000) = }')
