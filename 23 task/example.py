def doer(start, result):
    if result < start:
        return 0
    if result == start:
        return 1
    K = doer(start, result - 1)
    if result % 2 == 0:
        K += doer(start, result // 2)
    return K


print(doer(1, 10) * doer(10, 20))
