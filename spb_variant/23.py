from functools import lru_cache
from sys import setrecursionlimit
import threading

setrecursionlimit(99999999)


@lru_cache(99999999)
def f(s, e):
    if s < 0:
        return 0
    if s == e:
        return 1
    return f(s - 3, e) + f(s * (-3), e)


def main():
    print(333, 330)
    #if f(333, x) == 13:
     #   c += 1


if '__main__' == '__name__':
    threading.stack_size(200000000)
    thread = threading.Thread(target=main())
    thread.start()
