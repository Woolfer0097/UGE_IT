def f(x, a):
    return (x % 3 != 0) or (x % 2 != 0) or (x - a >= 4)


r = []
for A in range(1, 10**4):
    if all([f(X, A) for X in range(1, 10**4)]):
        r.append(A)

print(max(r))
