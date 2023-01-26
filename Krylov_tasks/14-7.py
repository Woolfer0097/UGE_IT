expr = 2 * 3**2022 + 5 * 3**1800 + 3**1001 + 4 * 3**1000 + 3


result = []
while expr > 0:
    rest = expr % 9
    expr //= 9
    result.append(str(rest))

result.reverse()
res = int("".join(result))
print(str(res).count("0"))
