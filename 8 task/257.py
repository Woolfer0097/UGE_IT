from itertools import product


count = 0
for index, i in enumerate(sorted(product("степуха", repeat=4))):
    if index > 1000:
        if i.count("с") < 2 and i.count("т") < 2 and \
                i.count("е") < 2 and i.count("п") < 2 and i.count("у") < 2 and \
                i.count("х") < 2 and i.count("а") < 2:
            count += 1

print(count)
