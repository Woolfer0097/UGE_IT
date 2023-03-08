# Сколько существует четырехзначных чисел, все цифры которых различны, не равны 0,
# и среди них есть по крайней мере одна четная и хотя бы одна нечетная?


odds = {'1', '3', '5', '7', '9 task'}
evens = {'2', '4', '6', '8'}
result = []

for i in range(1000, 10000):
    if len(set(list(str(i)))) == 4 \
            and str(i).count('0') == 0 \
            and len(set(str(i)) & odds) > 0 and len(set(str(i)) & evens) > 0:
        result.append(i)

print(len(result))
