import threading
from math import factorial
from functools import reduce, lru_cache
from sys import setrecursionlimit
import sys


@lru_cache(9999999)
def f(n):
    if n >= 5000:
        return factorial(n)
    if 1 <= n < 5000:
        return 2 * f(n + 1) // (n + 1)


def main():
    print(1000 * f(7) / f(4))


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(200000000)
    thread = threading.Thread(target=main)
    thread.start()
