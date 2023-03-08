import threading
from sys import setrecursionlimit
from functools import lru_cache


@lru_cache(200000)
def f(n):
    if n > 10000:
        return n - 10000
    if 1 <= n <= 10000:
        return f(n + 1) + f(n + 2)


def main():
    print(f(12345)*(f(10) - f(12)) / (f(11) + f(10101)))


if __name__ == '__main__':
    setrecursionlimit(1000000)
    threading.stack_size(20000000)
    thread = threading.Thread(target=main)
    thread.start()
