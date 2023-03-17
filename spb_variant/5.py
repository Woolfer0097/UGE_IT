for n in range(1, 100):
    r = bin(n)[2:]
    n_r = ""
    for i in r:
        if i == "0":
            n_r += "1"
        else:
            n_r += "0"
    r = "1" + n_r
    if r.count("1") % 2 == 0:
        r += "0"
    else:
        r += "1"
    r = int(r, 2)
    if r > 180:
        print(n)
        break
