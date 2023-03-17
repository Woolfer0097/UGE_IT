reg = iter([0] * 10)

iterations = 0


def f(x, y):
    return y


def Z(n):
    global reg

    reg = list(reg)
    reg[n] = 0
    reg = iter(reg)


def S(n):
    global reg

    reg = list(reg)
    reg[n] += 1
    reg = iter(reg)


def I(m, n, q):
    global iterations
    global reg

    reg = list(reg)
    if reg[m] == reg[n]:
        reg = iter(reg)
        while iterations < q:
            iterations += 1
            next(reg)


if __name__ == '__main__':
    I(2, 3, 5)
    S(1)
    S(3)
    I(1, 1, 1)
    reg = list(reg)
    print(reg)
    for x in reg:
        for y in reg:
            if reg[0] == f(x, y):
                print("ААААААААААА")
