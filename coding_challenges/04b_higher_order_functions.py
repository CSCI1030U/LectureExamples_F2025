# coding challenge 04b.1

def myfilter(check, data):
    result = []

    for item in data:
        if check(item):
            result.append(item)

    return result

marks = [64.5, 87.0, 55.5, 94.0, 71.5, 46.0, 100.0]
print(f'{myfilter(lambda mark: mark > 80.0, marks) = }')
# expected output: myfilter(lambda mark: mark > 80.0, marks) = [87.0, 94.0, 100.0]
