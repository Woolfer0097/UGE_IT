res = []

for x in range(26):
    if all([(int(f"13{y}{x}5", 26) + int(f"24{y}13", 26)) % 8 == 0 for y in range(26)]):
        res.append(x)

print((int(f"132{max(res)}5", 26) + int(f"24213", 26)) // 8)

