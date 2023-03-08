def f(s, e):
    if s < e:
        return 0
    if s == e:
        return 1
    return f(s, e + 2) * f(s, e * 3) * f(s, e * 4)


nums = [i for i in range(100, 601) if sum(map(int, list(str(i)))) % 11 == 0]
result = f(1, nums[0])
for k in range(len(nums[1:])):
    result *= f(nums[k], nums[k + 1])

print(result)
