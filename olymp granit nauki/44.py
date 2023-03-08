def foo(n):
    return 4 * (n + 11) * (n - 19) + 1


a = -10
b = 10
k = a
r = foo(a)
for j in range(a, b):
    if foo(j) < r:
        k = j
        r = foo(j)

print(k)
