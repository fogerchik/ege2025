from turtle import *
screensize(10_000,10_000)
tracer(0)
lt(90)
n = 20
for  i in range(10):
    fd(22*n)
    rt(90)
    fd(16*n)
    rt(90)
up()
fd(1*n)
rt(90)
fd(1*n)
lt(90)
down()
for  i in range(10):
    fd(72*n)
    rt(90)
    fd(79*n)
    rt(90)
up()
for x in range(-30,30):
    for y in range(-30, 30):
        goto(x*n,y*n)
        dot(3,'white')
update()
done()