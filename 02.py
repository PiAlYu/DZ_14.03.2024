print('x y z w f')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (w or x or (not(z)) or y)
                f = f and (w or x or (not(z)) or (not(y)))
                f = f and (w or (not(x)) or (not (z)) or (not (y)))
                if f == 0:
                    print(x, y, z, w, f)
