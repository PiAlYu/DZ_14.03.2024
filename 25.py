for i in range(10):
    for j in range(100):
        s = str(j)
        while len(s) < 3:
            s = '0' + s
        s = '123' + str(i) + '4' + s + '5679'
        s = int(s)
        if s % 4013 == 0:
            print(s, s // 4013)
for i in range(10):
    for j in range(1, 1000):
        s = '123' + str(i) + '4' + str(j) + '5679'
        s = int(s)
        if s % 4013 == 0:
            print(s, s // 4013)
