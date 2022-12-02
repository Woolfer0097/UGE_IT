# 298)	(В. Шубинкин) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1. Строится двоичная запись числа N.
# 2. Если количество единиц в этой записи чётно, стирается ведущая единица. В противном случае из записи числа убираются все нули, а в конец приписывается 1.
# 3. Над новой записью снова производятся действия, описанные в пункте 2.
# 4. Результат переводится в десятичную систему и выводится на экран.
# Например, N = 510 = 1012 => 1 => 112 = 310 = R.
# Сколько существует чисел N, не превосходящих 1000, таких что R = 7?

count = 0

for n in range(2, 1001):
    number = bin(n).replace("0b", "")
    for _ in range(2):
        if number.count("1") % 2:
            number = str(int(number[1:]))
        else:
            number = (number.count("1") + 1) * "1"
    count += int(number, 2) == 7

print(count)
