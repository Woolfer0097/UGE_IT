e = 3 ** 333 + 3 ** 22 - 9 ** 111 - 8


count = 0
while e > 0:
    if e % 3 == 2:
        count += 1
    e //= 3


print(count)
