# 2
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not (z <= y)) or (x <= w) or (not x)
                if f == 0:
                    print(x, y, z, w)
# 5
ans = []
for N in range(1, 10_000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '10' + R
    else:
        R = '1' + R + '01'
    R = int(R, 2)
    R = print(R, 2)
    if N <= 12:
        ans.append(R)
print(max)
