expr = 3 ** 2021 + 5 * 3 ** 2000 + 3 ** 501 + 5 * 3 ** 500 + 1

result = []
while expr > 0:
    result.append(str(expr % 9))
    expr //= 9

num = int("".join(result))
print(str(num).count("0"))
