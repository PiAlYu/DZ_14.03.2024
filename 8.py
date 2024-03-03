from itertools import product

k = 1
for i in product('гекэ023', repeat = 4):
    s = ''.join(i)
    if s[0] in '023' and all((i * 2) not in s for i in 'гекэ023'):
        print(k)
        break
    k += 1
