c = 0
for n in range(10 ** 4, 10 ** 5):
    even = [int(i) for i in str(n) if int(i) % 2 == 0]
    odds = [int(i) for i in str(n) if int(i) % 2 != 0]
    if str(n).count("6") == 1 and sum(even) < sum(odds):
        c += 1

print(c)
