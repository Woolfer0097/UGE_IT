from math import sqrt


def f(n):
    if 1 <= sqrt(n) == int(sqrt(n)):
        return sqrt(n)
    if type(sqrt(n)) == float:
        return f(n + 1) + 1


print(f(4850) + f(5000))
