def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


for n in range(1, 30):
    s = ">" + 15 * "0" + n * "1" + 15 * "2"
    while ">0" in s or ">1" in s or ">2" in s:
        if ">0" in s:
            s = s.replace(">0", "22>", 1)
        elif ">1" in s:
            s = s.replace(">1", "2>", 1)
        elif ">2" in s:
            s = s.replace(">2", "1>", 1)
    if isPrime(sum(list(map(int, s.strip(">"))))):
        print(n)
        break
