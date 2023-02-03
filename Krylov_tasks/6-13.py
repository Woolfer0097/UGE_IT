import turtle
from math import sqrt
from turtle import *

speed(0)
k = 100
color("black", "green")
begin_fill()
lt(90)
rt(60)
for i in range(4):
    fd(8 * k)
    rt(120)
    fd(4 * k)
    rt(240)
rt(120)
fd(2 * k)
rt(90)
fd(16 * sqrt(3) * k)
rt(90)
fd(2 * k)
end_fill()
canvas = getcanvas()
count = 0

for y in range(-100 * k, 100 * k, k):
    for x in range(-100 * k, 100 * k, k):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1

print(count)
done()
exit()
