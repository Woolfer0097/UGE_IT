rangement = range(150, 200)

count = 0
for n in range(2, 100):
    result = ""
    number = bin(n)[2:]
    result += number
    result += number[-2]
    result += number[1]
    if int(result, 2) in rangement:
        count += 1

print(count)
