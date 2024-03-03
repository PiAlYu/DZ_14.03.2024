fin = open('27B.txt')
s = fin.readlines()
fin.close()
s.pop(0)
s = [list(map(int, i.split())) for i in s]
for i in s:
    i.append(abs(i[0] - i[1]))
s.sort(key = lambda x: x[2])
a = []
for i in s:
    a.append(max(i))
for i in range(len(a)):
    if s[i][0] % 2 != s[i][1] % 2:
        if s[i][0] == a[i]:
            a.pop(i)
            a.append(s[i][1])
        else:
            a.pop(i)
            a.append(s[i][0])
        break
print(sum(a))
