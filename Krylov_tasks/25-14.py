def check(num):
    dels = [i for i in range(num - 1, 0, -1) if num % i == 0]
    for i in range(num - 1, 0, -1):
        if num % i == 0 and len(dels) > 3:
            return i


count = 0
number = 550000

while count < 6:
    max_gcd = check(number)
    if max_gcd:
        count += 1
        print(number, max_gcd)
    number += 1
