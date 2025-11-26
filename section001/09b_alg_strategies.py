# 09b - Algorithm Strategies

def dc_search(elements, to_find):
    if len(elements) == 0:
        return False 
    elif len(elements) == 1:
        return elements[0] == to_find
    
    # print(f'{elements = }')

    # divide
    mid = len(elements) // 2
    first = elements[:mid]
    second = elements[mid:]

    # conquer (recursively solve)
    first_result = dc_search(first, to_find)
    second_result = dc_search(second, to_find)

    # combine
    return first_result or second_result

print(f'{dc_search([1,2,3,4,5,6,7,8], 5) = }')
print(f'{dc_search([1,7,4,8,3,2,5,6], 5) = }')
print(f'{dc_search([1,7,4,8,3,2,5,6], 15) = }')
print(f'{dc_search([1,7,4,8,3,2,5,6], 1) = }')
print(f'{dc_search([1,7,4,8,3,2,5,6], 6) = }')

# coding exercise 09b.2
def insert_sort_by_ratio(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i]['ratio'] < key['ratio']:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key


def greedy_knapsack(available_items, max_weight):
    # calculate the value/weight for all items
    value_to_weight = []
    for item in available_items:
        value_to_weight.append({
            'name': item['name'],
            'value': item['value'],
            'weight': item['weight'],
            'ratio': item['value'] / item['weight']
        })
    
    # sort by value/weight in descending order
    insert_sort_by_ratio(value_to_weight)
    # print(f'{value_to_weight = }')

    # choose the items from highest ratio until backpack is full
    backpack = []
    for item in value_to_weight:
        if item['weight'] <= max_weight:
            # take the whole item
            backpack.append(item)
            max_weight -= item['weight']
        else:
            # take the max fraction of this item
            fraction = max_weight / item['weight']
            partial_item = {
                "name": item["name"],
                'weight': item['weight'] * fraction,
                'value': item['value'] * fraction,
                'ratio': item['ratio']
            }
            backpack.append(partial_item)
            # max_weight -= item['weight'] * fraction
            return backpack



items = [
    {
        'name': 'Wooden Sculpture',
        'weight': 2.0,
        'value': 3.5
    },
    {
        'name': 'Silver Earrings',
        'weight': 1.0,
        'value': 150.0
    },
    {
        'name': 'Diamond Necklace',
        'weight': 1.0,
        'value': 750.0
    },
    {
        'name': 'Stone Statue',
        'weight': 45.0,
        'value': 8.5
    },
    {
        'name': 'Gold Bracelet',
        'weight': 5.0,
        'value': 275.0
    },
]
print(f'{greedy_knapsack(items, 8.5) = }')

# coding exercise 09b.3
def fib_dp(n: int) -> int:
    solutions: list[int] = [0, 1]
    if n < 2:
        return solutions[n]
    for i in range(2, n + 1):
        solutions.append(solutions[i - 1] + solutions[i - 2])
    return solutions[n]

print(f'{fib_dp(100) = }')
