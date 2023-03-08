print("x y z w F")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                r = (x or y) and (not y == z) and w
                if r:
                    print(x, y, z, w, r)
