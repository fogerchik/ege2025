from sys import setrecursionlimit
def f(n):
    if n >= 2010:
        return n
    if n < 2010:
        return f(n+3)+f(n+2)+f(n+1)
setrecursionlimit(12765756)
print((f(2000)-2*(f(2002)+f(2003)))/f(2004))



def f(cur, end):
    if cur == end: return 1
    if cur > end or cur == 9: return 0
    return f(cur +1, end) + f( cur *2, end)
print (f(2,12)*f(12,42))



