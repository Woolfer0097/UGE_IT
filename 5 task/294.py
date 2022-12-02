result = []

for n in range(1000, 10000):
    if n % 2 == 0:
        r = int("".join(map(str, sorted([int(i) for i in str(n)], reverse=True)))) // 2
    else:
        r = int("".join(map(str, sorted([int(i) for i in str(n)])))) // 2
    if r - n == 1:
        result.append(r)

print(min(result))
