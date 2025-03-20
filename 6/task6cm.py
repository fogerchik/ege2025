from turtle import *

tracer(0)
lt(90)
n = 10
for i in range(10):
    fd(22 * n)
    rt(90)
    fd(16 * n)
    rt(90)
up()
fd(1 * n)
rt(90)
fd(1 * n)
lt(90)
down()
for i in range(10):
    fd(72 * n)
    rt(90)
    fd(79 * n)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * n, y * n)
        dot(6, 'white')
update()
done()
