from turtle import *

tracer(0)
rt(270)
n = 10
for i in range(2):
    fd(10 * n)
    rt(90)
    fd(18 * n)
    rt(90)
up()
fd(5 * n)
rt(90)
fd(7 * n)
lt(90)
down()
for i in range(2):
    fd(10 * n)
    rt(90)
    fd(7 * n)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * n, y * n)
        dot(3,"red" )
update()
done()
