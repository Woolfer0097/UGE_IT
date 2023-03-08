# from random import sample
#
s = ">" + "1" * 10 + "2" * 20 + "3" * 30
# s = ">" + ''.join(sample(s, len(s)))
# print(s)
# РЕЗУЛЬТАТ НЕ ЗАВИСИТ ОТ ИЗНАЧАЛЬНОГО РАСПОЛОЖЕНИЯ ЦИФР


while ">1" in s or ">2" in s or ">3" in s:
    if ">1" in s:
        s = s.replace(">1", "22>", 1)
    if ">2" in s:
        s = s.replace(">2", "2>", 1)
    if ">3" in s:
        s = s.replace(">3", "1>", 1)


print(sum(list(map(int, s.strip(">")))))

# 140 - CORRECT
