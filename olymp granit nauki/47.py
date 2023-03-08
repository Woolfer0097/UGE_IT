n = [1, 2, 7, 3, 6, 1, 4, 5, 3, 5, 3, 21]
m = []
for k in range(len(n)):
    if k >= n[k]:
        m.append(n[k])

print(m)
print(max(m))
print(m.count(max(m)))
