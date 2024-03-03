fin = open('09.csv')
s = fin.readlines()
fin.close()
k = 0
s = [list(map(int, i.split(';'))) for i in s]
for i in s:
    if all(j < sum(i) - j for j in i) and sum(i) == 360:
        k += 1
print(k)
