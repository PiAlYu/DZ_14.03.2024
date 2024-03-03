from functools import lru_cache

def moves(h):
    a, b = h
    return (a + b, b), (a, b + a)

@lru_cache(None)
def game(h):
    if sum(h) >= 57:
        return 'end'
    if any(game(i) == 'end' for i in moves(h)):
        return 'p1'
    if any(game(i) == 'p1' for i in moves(h)):
        return 'v1'

for i in range(1, 48):
    if game((10, i)) == 'v1':
        print(i, game((10, i)))
        break
