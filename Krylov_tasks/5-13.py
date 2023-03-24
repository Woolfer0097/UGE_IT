res = []
for n in range(1, 100):
    n -= n % 8
    n += n % 2
    r = bin(n)[2:]
    r += f"{r.count('1') % 2}"
    r += f"{r.count('1') % 2}"
    if int(r, 2) > 90:
        print(int(r, 2))
        break
