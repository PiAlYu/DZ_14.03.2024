def f(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n = n // 5
    return s

a = 5 ** 2004 - 5 ** 1016 - 25 ** 508
a += - 5 ** 400 + 25 ** 250 - 27
print(f(a).count('4'))
