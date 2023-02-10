e = 7 * 729**6 + 6 * 81**9 + 3**14 - 90

count = 0
while e > 0:
    if e % 2 == 0:
        count += 1
    e //= 2

print(count)
