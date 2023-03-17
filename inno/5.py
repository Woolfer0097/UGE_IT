print("f\trf\tg\trg")
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            f = int(x1 and x2 or x2 and x3 or x3 and x1)
            g = int(x1 != x2 != x3 != 1)
            rf = int(not x1 or not x2 and not x2 or not x3 and not x3 or not x1)
            rg = int(x1 & x2 & x3 & 1)
            if f == rf:
                print("F IS SELF-DUAL")
            else:
                print("F IS NOT SELF-DUAL")
            if g == rg:
                print("g IS SELF-DUAL")
            else:
                print("g IS NOT SELF-DUAL")

            print(f, rf, g, rg, sep="\t")
