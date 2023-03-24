for a in range(1, 1000):
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            if not((2 * y + 4 * x < a) or (x + 2 * y > 80)):
                flag = False

    if flag:
        print(a)
        break
