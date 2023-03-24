for a in range(1, 1000):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not((2 * y + 5 * x < a) or (x + y > 80)):
                flag = False
    if flag:
        print(a)
        break
