from turtle import *
screensize(10_000,10_000)
tracer(0)
lt(90)
n = 20
for i in range (3):
    fd(7*n)
    rt(90)
    fd(12*n)
    rt(90)
up()
fd(4*n)
rt(90)
fd(6*n)
lt(90)
down()
for i in range (4):
    fd(83*n)
    rt(90)
    fd(77*n)
    rt(90)
up()
for x in range(-30,30):
    for y in range(-30, 30):
        goto(x*n,y*n)
        dot(3,'red'
              '')
update()
done()