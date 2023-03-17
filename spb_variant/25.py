from fnmatch import fnmatch

for x in range(1, 10 ** 10):
    number = fnmatch(str(x), "1?2139*4")
    if number % 3052 == 0:
        print(number, number // 3052)
