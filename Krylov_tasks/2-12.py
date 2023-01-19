print("x y z w")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                result = (not z or x) and (not w and y)
                if result:
                    print(x, y, z, w)
