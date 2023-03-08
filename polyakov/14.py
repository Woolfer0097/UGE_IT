def t(n, base):
    res = []
    length = len(n)
    for i in range(length):
        res.append(int(n[i]) * (base ** (length - 1 - i)))
    return sum(res)


end = []
for x in range(2, 157):
    n1 = [2, 7, 3, x, 2]
    n2 = [1, x, 3, 9, 0]
    result = t(n1, 158) + t(n2, 158)
    if result % 73 == 0:
        end.append(result // 73)


print(sum(end))
