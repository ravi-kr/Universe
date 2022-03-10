tests = []
test = {
        'input': {
                'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
                'query' : 7
                },
        'output': 3
        }
tests.append(test)

tests.append({
    'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0],
              'query': 1},
    'output':6})

tests.append({
    'input': {'cards': [4, 2, 1, -1],
              'query': 4},
    'output':0})

tests.append({
    'input': {'cards': [3, -1, -9, -127],
              'query': -127},
    'output':3})

tests.append({
    'input': {'cards': [6],
              'query': 6},
    'output':0})

tests.append({
    'input': {'cards': [9, 7, 5, 2, -9],
              'query': 4},
    'output':-1})

tests.append({
    'input': {'cards': [],
              'query': 7},
    'output':-1})

tests.append({
    'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
              'query': 3},
    'output':7})

tests.append({
    'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
              'query': 6},
    'output':2})

#print(tests)

def locate_card(cards, query):
    position = 0
    print('cards: ', cards)
    print('query: ', query)
    
    while position < len(cards):
        print('position: ', position)
        if cards[position] == query:
            return position
        position += 1
    return -1
        
result = locate_card(test['input']['cards'], test['input']['query'])
print(result)
print(result == test['output'])
#assert locate_card(**test['input']) == test['output']

def evaluate_test_cases(function, test_cases):
    for i in range(len(test_cases)):
        if function(**test_cases[i]['input']) == test_cases[i]['output']:
            result = 'Passed'
        else:
            result = 'Failed'
        print(f"Test case {i+1} is " + result)
        
evaluate_test_cases(locate_card, tests)

#cards6 = tests[6]['input']['cards']
#query6 = tests[6]['input']['query']
#locate_card(cards6, query6)

def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card_binary(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

evaluate_test_cases(locate_card_binary, tests)

