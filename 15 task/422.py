def f(x, a):
    return (x % 3 != 0 and x not in (48, 52, 56)) <= ((abs(x - 50) <= 7) <= (x in range(29, 48))) or (x & a == 0)


for a in range(1, 100):
    if all([f(x, a) for x in range(1, 1000)]):
        print(a)
        break
