from copy import copy

def discount(z):
    if z == 5:
        return 5 * 0.75
    elif z == 4:
        return 4 * 0.8
    elif z == 3:
        return 3 * 0.9
    elif z == 2:
        return 2 * 0.95
    else:
        return 1

def new_state(books_state, k):
    x = [int(el > 0) for el in books_state]
    if sum(x) >= k:
        for i in range(k):
            books_state[i] -= 1
        return books_state
    else:
        for i in range(sum(x)):
            books_state[i] -= 1
        return new_state(books_state, k-sum(x))

def min_cost(books_state, k):
    if sum(books_state) < k:
        return float('Inf')
    x = [int(el > 0) for el in books_state]
    if sum(x) >= k:
        return discount(k)
    else:
        for i in range(sum(x)):
            books_state[i] -= 1
        return discount(sum(x)) + min_cost(books_state, k-sum(x))
    
books = [5, 3, 4, 2, 2, 3, 1]
books = sorted(books)[::-1]

N = sum(books)
state = [[0] * 5 for _ in range(N+1)]
price = [0] * (N + 1)
state[0] = books
books = sorted(books)[::-1]
price[0] = 0
state[0] = copy(books)
i = 1

while True:
    v = []
    for j in range(1, min(i+1, 6)):
        v.append(price[i-j] + min_cost(state[i-j], j))
    idx = v.index(min(v))
    price[i] = v[idx]
    state[i] = new_state(copy(state[i-idx-1]), idx+1)
    if sum(state[i]) == 0:
        break
    state[i] = sorted(state[i])[::-1]
    i += 1

print(price[-1])