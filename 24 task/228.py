with open("24data/24-228.txt", "r") as f:
    string = f.readline()

res = []
while string.find("XX"):
    index1 = string.find("XX")
    str_for_check = string[index1+2:index1+13]
    if str_for_check[0] == "3" and str_for_check[5:7] == "78" and str_for_check[9:11] == "45":
        res.append(int(str_for_check))

    string = string[index1+14:]

res1 = 1
res2 = 0
for i in str(max(res)):
    if int(i) % 2 != 0:
        res2 += int(i)
    else:
        res1 *= int(i)

print(res1 + res2)
