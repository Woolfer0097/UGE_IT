def get_divs(x):
    return [y for y in range(2, x) if x % y == 0]


def isPrime(x):
    return len(get_divs(x)) == 1


i = 450_000
count = 0

while count < 6:
    gcd_ = max(get_divs(i))
    print(get_divs(gcd_))
    if gcd_ != i and not isPrime(gcd_):
        print(i, gcd_)
        count += 1
    i += 1
