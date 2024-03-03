def f(a):
    for x in range(100):
        for y in range(100):
            f = (2 * x + 3 * y != 150) or (x < a) and (y < a)
            if f == False:
                return False
    return True

for s in range(1, 100):
    if f(s) == True:
        print(s)
        break
