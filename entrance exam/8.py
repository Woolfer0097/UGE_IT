numbers = []

e1 = 2 ** 16
e2 = 4 ** 16
e3 = 8 ** 16

for i in range(2, 10000000):
    if 2 ** i <= e1:
        numbers.append(2 ** i)
    else:
        break

for i in range(2, 1000000):
    if 4 ** i <= e2:
        numbers.append(4 ** i)
    else:
        break

for i in range(2, 10000000):
    if 8 ** i <= e3:
        numbers.append(8 ** i)
    else:
        break

numbers.sort()

print(numbers[:32])
