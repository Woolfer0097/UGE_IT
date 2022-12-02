count = 0
for n in range(100000000, 1000000000):
    r = sum(map(int, str(n).split()))
    r = bin(r)[2:]
    if r.count("1") % 2 == 0:
        r = f"1{r}00"
    else:
        r = f"10{r}1"
    if int(r, 2) == 21:
        count += 1

print(count)

# СЛИШКОМ ДОЛГО
