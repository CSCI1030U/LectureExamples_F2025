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
def greedy_knapsack(available_items, max_weight):
    pass 

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