first = set()
second = set()

for k in range(100):
    y = 0
    for x in range((k + 6) // 2, (2 * k + 16) // 2):
        y += abs(x)
        first.add(y)

for k in range(100):
    y = 0
    for x in range((2 * k + 16) // 2, (k + 6) // 2, -1):
        y += abs(x)
        second.add(k)

k = 3
y = 0
for x in range((2 * k + 16) // 2, (k + 6) // 2, -1):
    y += abs(x)
print(y)
y = 0
for x in range((k + 6) // 2, (2 * k + 16) // 2):
    y += abs(x)
print(y)
print(first & second)
