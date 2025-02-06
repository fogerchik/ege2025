from turtle import *

tracer(0)
screensize(1000,1000)
rt(270)
n = 20
for i in range(9):
    fd(22 * n)
    rt(90)
    fd(6 * n)
    rt(90)
up()
fd(1 * n)
rt(90)
fd(5 * n)
lt(90)
down()
for i in range(9):
    fd(53 * n)
    rt(90)
    fd(75 * n)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * n, y * n)
        dot(3, "red")
update()
done()
