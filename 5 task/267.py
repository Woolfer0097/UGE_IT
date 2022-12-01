for n in range(1, 100):
    number = [("0", "1")[i == "0"] for i in bin(n)[2:]]
    if n % 2 != 0 and int("".join(number), 2) + n > 99:
        print(n)
        break