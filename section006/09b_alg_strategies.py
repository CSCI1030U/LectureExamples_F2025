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
