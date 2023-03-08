print("x y z w F")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                r = (not x and y) or (z and not y) or (not z and w)
                if not r:
                    print(x, y, z, w, int(r))
