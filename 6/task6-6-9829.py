from turtle import *

tracer(0)
rt(180)
n = 10
for i in range(3):
    rt(45)
    fd(10 * n)
    rt(45)
rt(315)
fd(10 * n)
for i in range(2):
    rt(90)
    fd(10 * n)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * n, y * n)
        dot(3, "red")
update()
done()
