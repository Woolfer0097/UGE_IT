from turtle import *

speed(0)
m = 5
color("black", "red")
begin_fill()
lt(90)
rt(10)
fd(4 * m)
rt(90)
fd(48 * m)
rt(90)
fd(4 * m)
rt(30)
for i in range(8):
    fd(6 * m)
    rt(120)
    fd(6 * m)
    rt(240)
end_fill()
canvas = getcanvas()
count = 0
for y in range(-100 * m, 100 * m, m):
    for x in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1

print(count)
done()
exit()
