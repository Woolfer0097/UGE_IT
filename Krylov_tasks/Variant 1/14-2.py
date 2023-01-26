expression = 4**2022-6*4**522+5*64**510-3*2**330-100
count = 0
result = ""

while expression > 0:
    rest = expression % 8
    expression //= 8
    result += str(rest)

print(result.count("7"))
