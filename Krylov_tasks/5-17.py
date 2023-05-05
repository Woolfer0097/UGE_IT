for n in range(1, 10):
    r = bin(n)[2:]
    r = r.replace("0", "01").replace("1", "10")
    if int(r, 2) > 63:
        print(n, int(r, 2))
        break
