from itertools import permutations
graph='BA AE EC CD DF FH HB HA EG CG GF'.split()
matrix='247 148 578 126 38 47 136 235'.split()
print(*range(1,9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)


#6)
from turle import *

tracer(0)
screensize(1000,1000)
rt(270)
n = 20
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
        dot(8, "white")
update()
done()
#16
from sys import setrecursionlimit
def f(n):
    if n > 7000:
        return n+4
    if n <= 7000:
        return 3*n +5 +f(n+3)
setrecursionlimit(8000)
print(f(707)-f(716))
