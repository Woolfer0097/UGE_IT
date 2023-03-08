def foo(x):
    if x % 3 == 0:
        return 6 + x * 4 - 2
    return 3 - x + 3 * x


a = -7
b = 13
k = a
r = foo(a)
for j in range(a, b - 1):
    if foo(j) < r:
        k = j
        r = foo(j)

print(k)
