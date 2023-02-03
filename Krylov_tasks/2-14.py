print("w x y z R")

for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                result = int(((w == (not y)) or (w == (not z))) and x and (not y or z))
                if result == 1:
                    print(w, x, y, z, result)
