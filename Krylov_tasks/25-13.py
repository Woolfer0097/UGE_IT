def f(n):
    divisors = [i for i in range(1, n - 1) if n % i == 0]
    if divisors:
        return max(divisors) - min(divisors)
    return 0


count = 0
for j in range(850000, 10000000):
    if count == 6:
        break
    if f(j) != 0 and f(j) % 13 == 0:
        count += 1
        print(j, f(j))
