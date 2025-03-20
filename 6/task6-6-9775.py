from turtle import *

tracer(0)
rt(270)
n = 10
for i in range(2):
    fd(13 * n)
    rt(90)
    fd(20 * n)
    rt(90)
up()
fd(8 * n)
rt(90)
bk(3 * n)
lt(90)
down()
for i in range(2):
    fd(16 * n)
    rt(90)
    fd(8 * n)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * n, y * n)
        dot(3, "red")
update()
done()
