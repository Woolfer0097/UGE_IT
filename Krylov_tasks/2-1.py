print("x y z w R")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # res = y and (not x or w) and (x or (not w == z))
                res = w and y and x or not x and y and not w == z
                print(x, y, z, w, int(res))
