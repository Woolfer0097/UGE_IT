for n in range(1, 100):
    number = hex(n // 2)[2:]
    if n % 4 != 0:
        number = f"F{number}A0"
    else:
        number = f"15{number}C"
    if int(number, 16) < 65536:
        print(n)
