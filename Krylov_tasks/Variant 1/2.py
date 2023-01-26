print("x y z w R")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                result = x and ((not y) or z) and (y or ((not z) == w))
                print(x, y, z, w, int(result))
