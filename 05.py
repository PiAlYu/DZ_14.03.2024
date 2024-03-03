for n in range(1, 100):
    r = bin(n)[2:]
    s = sum([int(i) for i in r])
    if s % 2 == 1:
        r = r + '11'
    else:
        r = '11' + r
    r = int(r, 2)
    if r > 102:
        print(n)
        break
