res = []
even = [i for i in range(0, 10) if i % 2 == 0]
odd = [j for j in range(0, 10) if j % 2 != 0]
for ch in even:
    for n in odd:
        for q in range(0, 10):
            if int(f"11{ch}{q}{q}{n}11") % 2023 == 0:
                res.append(int(f"11{ch}{q}{q}{n}11"))

print(len(res))
res.sort()
for i in res:
    print(i, i // 2023)
