expr = 4**2022 - 2 * 4**1111 + 16**600 + 192

count = 0
while expr > 0:
    rest = expr % 4
    expr //= 4
    if rest == 3:
        count += 1

print(count)
