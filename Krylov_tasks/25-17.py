def gd(n):
    return max([i for i in range(1, n - 1) if n % i == 0])


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


count = 0
num = 650_000
while count < 6:
    num += 1
    if gd(num) != num and not isPrime(gd(num)):
        print(num, gd(num))
        count += 1
