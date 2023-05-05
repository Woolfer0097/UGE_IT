def gd(n):
    return max([i for i in range(1, n) if n % i == 0])


def is_prime(m):
    return len([i for i in range(2, m) if m % i == 0]) == 0


for x in range(350_000, 10 ** 10):
    if gd(x) != x and not is_prime(gd(x)):
        print(x, gd(x))
