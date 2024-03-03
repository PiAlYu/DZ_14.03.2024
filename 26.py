fin = open('26.txt')
a = fin.readlines()
fin.close()
s, n = list(map(int, a.pop(0).split()))
a = [int(i) for i in a]
a.sort()
k = 0
for i in range(len(a)):
    if s > a[-i - 1]:
        k += 1
        s -= a[-i - 1]
        n = a[-i - 1]
    else:
        break
    if s > a[i]:
        k += 1
        s -= a[i]
        n = a[i]
    else:
        break
print(k, n)
