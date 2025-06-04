from turtle import *
screensize(10_000,10_000)
tracer(0)
lt(90)
n = 20
rt(90)
for i in range (3):
    rt(45)
    fd(10*n)
    rt(45)
up()
rt(315)
fd(10*n)
down()
for i in range (2):
    rt(90)
    fd(10*n)
up()
for x in range(-30,30):
    for y in range(-30, 30):
        goto(x*n,y*n)
        dot(3,'red'
              '')
update()
done()