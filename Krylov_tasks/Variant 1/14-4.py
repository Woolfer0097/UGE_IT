expr = 1331**650-55*121**610+7711**510-3*11**100-221
res = []

while expr > 0:
    rest = expr % 11
    expr //= 11
    res.append(rest)

print(res.count(10))
