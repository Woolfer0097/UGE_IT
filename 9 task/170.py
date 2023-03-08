import csv

res_data = []
with open("9-170.csv", "r") as csvf:
    data = csv.reader(csvf)
    for i in data:
        res_data.append(list(map(int, "".join(i).split(";"))))

count = 0
for s in res_data:
    repeated = False
    flag = False
    rep = False
    for i in set(s):
        if s.count(i) == 2:
            if repeated:
                flag = True
                break
            else:
                rep = i
                repeated = True
    if flag:
        break
    if rep and (sum(set(s)) // len(set(s))) < rep * s.count(rep):
        count += 1

print(count)


# 2241 - answer
