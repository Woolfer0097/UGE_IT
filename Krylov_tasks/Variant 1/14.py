expression = 4*25**2022-2*5**2000+125**1011-3*5**100-660
count = 0


while expression > 0:
    rest = expression % 5
    expression //= 5
    if rest == 4:
        count += 1

print(count)
