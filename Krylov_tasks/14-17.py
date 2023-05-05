r = 7**80+49**15-49

res = ""
while r > 0:
    res += str(r % 7)
    r //= 7
print(res.count("6"))
