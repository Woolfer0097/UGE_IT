count = 0
for n in range(100):
    r = bin(n)[2:]
    summa = sum(map(int, list(r)))
    r += str(summa % 2)
    summa = sum(map(int, list(r)))
    r += str(summa % 2)
    result = int(r, 2)
    if result < 50:
        count += 1


print(count)
