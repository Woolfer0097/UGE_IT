r = []
for x in range(3, 100):
    t = []
    for y in range(2, x):
        if x % y == 0:
            t.append(x)
        if len(t) == 3:
            print(x)
            break