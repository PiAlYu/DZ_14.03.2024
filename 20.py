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
    if all(game(i) == 'p1' for i in moves(h)):
        return 'v1'
    if any(game(i) == 'v1' for i in moves(h)):
        return 'p2'

for i in range(1, 48):
    if game((9, i)) == 'p2':
        print(i, game((10, i)))
