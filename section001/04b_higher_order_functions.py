# 04b - Higher Order Functions

def a(message: str) -> None:
    print(f'a:{message}')

def b(message: str) -> None:
    print(f'b:{message}')
    a('the arg from b')

def c(message: str) -> None:
    print(f'c:{message}')
    b('the arg from c')

c('hello')

def traverse(elements, op):
    for element in elements:
        op(element)

def print_double(x):
    print(2 * x)

traverse([1,2,3], print_double)

# map()


def get_rank(score):
    thresholds = [100, 200, 300, 400, 500]
    ranks = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Ruby', 'Diamond']
    for i in range(len(thresholds)):
        if score < thresholds[i]:
            return ranks[i]
    return ranks[-1]

player_scores = [740, 17, 250, 420]
player_ranks = map(get_rank, player_scores)

print(f'{list(player_ranks) = }')
