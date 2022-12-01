def trans_to4(num):
    result = []
    while num // 4 > 0:
        rest = num % 4
        num //= 4
        result.append(str(rest))
    return result[::-1]


for n in range(4, 1000):
    number = trans_to4(n)
    if n % 2 != 0:
        number.insert(0, "2")
        number.append("11")
    else:
        number.insert(0, "13")
        number.append("02")

    if int("".join(number), 4) > 1000:
        print(int("".join(number), 4))
