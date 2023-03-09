from functools import reduce


with open("24data/24-228.txt", "r") as f:
    string = f.readline()

res = []
while string.find("XX"):
    index1 = string.find("XX")
    str_for_check = string[index1+2:index1+13]
    if str_for_check[0] == "3" and str_for_check[5:7] == "78" and str_for_check[9:11] == "45":
        res.append(int(str_for_check))

    string = string[index1+14:]

res_n = max(res)
print(sum([i for i in list(map(int, list(str(res_n)))) if i % 2 != 0]) +
      reduce(lambda acc, x: acc * x, filter(lambda x: x % 2 == 0, map(int, list(str(res_n))))))
