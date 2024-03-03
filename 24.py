fin = open('24.txt')
s = fin.readline()
fin.close()
print(s)
c, k = -1, -1
for i in range(1, len(s) - 1):
    if s[i] == s[i + 1]:
        k = max(k, c)
        c = -1
    else:
        c += 1
k = max(k, c)
print(k)
