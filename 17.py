fin = open('17 (1).txt')
s = fin.readlines()
fin.close()
s = [int(i) for i in s]
print(s)
ma, k, ma2 = 0, 0, 0
for i in s:
    if i % 17 == 0:
        ma = max(ma, i)
for i in range(len(s) - 1):
    if sum(s[i:i + 2]) > ma:
        k += 1
        ma2 = max(ma2, sum(s[i:i + 2]))
print(k, ma2)
