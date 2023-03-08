for n in range(1, 100):
    r = bin(n)[2:]
    if sum(map(int, list(r))) % 2 == 0:
        r += "0"
        r = "10" + r[2:]
    else:
        r += "1"
        r = "11" + r[2:]
    if int(r, 2) > 40:
        print(n)
        break
