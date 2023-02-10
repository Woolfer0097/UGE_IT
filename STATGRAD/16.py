def f(a, b):
    if a == 0:
        return b
    if a > 0:
        return f(a // 10, 10 * b + (a % 10))


for i in range(4623618421, 10 ** 11):
    if f(i, 0) == 1248163264:
        print(i)
        break
