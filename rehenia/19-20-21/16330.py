def f(x, y, s):
    if x + y >= 59: return s % 2 == 0
    if s ==0: return False
    h = [f(x + 1, y, s - 1),
         f(x, y + 1, s - 1),
         f(x * 2, y, s - 1),
         f(x, y * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

print("19)",[s for s in range(1, 53) if f(6, s, 2)])
print('20)',[s for s in range(1, 53) if f(6, s, 3)and not f(6,s,1)])
print('21)',[s for s in range(1, 53) if f(6, s, 4)and not f(6,s,2)])


# 1ОДНАКУЧА +7 *3  >=342 1<=S<=300 ВНАЧАЛЬЫНЙ МОМЕНТ
def f(a, m):
    if a >= 342:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 7, m - 1), f(a * 3, m - 1)]
    if (m - 1) % 2 == 0:
        return any(h)
    else:
        return all(h)


for s in range(1, 301):
    if f(s, 1) == 0 and f(s, 2) == 0 and f(s, 3) == 0 and f(s, 4) == 1 :
        print(s)

