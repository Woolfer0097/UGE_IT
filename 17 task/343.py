with open("17data/17-343.txt", "r") as f:
    data = list(map(int, f.readlines()))

res = []
for i in range(len(data) - 2):
    p1 = data[i]
    p1_1 = int(str(p1)[0])
    p1_2 = int(str(p1)[1])
    p1_3 = int(str(p1)[2])
    p1_4 = int(str(p1)[3])
    p2 = data[i + 1]
    p2_1 = int(str(p2)[0])
    p2_2 = int(str(p2)[1])
    p2_3 = int(str(p2)[2])
    p2_4 = int(str(p2)[3])
    p3 = data[i + 2]
    p3_1 = int(str(p3)[0])
    p3_2 = int(str(p3)[1])
    p3_3 = int(str(p3)[2])
    p3_4 = int(str(p3)[3])
    if ((p1_3 + p1_1) % (p1_4 + p1_2) == 0) and \
            ((p2_3 + p2_1) % (p2_4 + p2_2) == 0) and \
            ((p3_3 + p3_1) % (p3_4 + p3_2) == 0):
        res.append(p1 + p2 + p3)

print(len(res), min(res))
