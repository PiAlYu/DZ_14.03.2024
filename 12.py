n, mi2 = 201, float('inf')
for i in range(101, 201):
    s = '3' * i
    while '111' in s or '333' in s:
        if '111' in s:
            s = s.replace('111', '3', 1)
        else:
            s = s.replace('333', '1', 1)
    if int(s) < mi2:
        mi2 = int(s)
        n = i
print(n)
