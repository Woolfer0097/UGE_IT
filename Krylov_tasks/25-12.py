def dels(n):
    result_dels = []
    for i in range(2, n - 1):
        if n % i == 0:
            result_dels.append(i)
    return result_dels


count = 0
j = 850000
f = 0

while count < 6:
    if dels(j):
        f = max(dels(j)) - min(dels(j))
    else:
        f = 0
    if f != 0 and f % 11 == 0:
        print(j, f)
        count += 1
    j += 1
