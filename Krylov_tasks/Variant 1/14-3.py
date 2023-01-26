expression = 243**540-6*9**530+21*3**511-3*3**70-200

res = ""

while expression > 0:
    rest = expression % 9
    expression //= 9
    res += str(rest)


print(res.count("8"))
