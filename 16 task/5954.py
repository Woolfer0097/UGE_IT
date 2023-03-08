from functools import lru_cache
from sys import setrecursionlimit


setrecursionlimit(999999)


@lru_cache(99999)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)


print((f(2023) - f(2022)) / f(2020))
