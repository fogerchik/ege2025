ans = []
for N in range(1, 10_000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + '1'
    else:
        R = R + bin(N % 3 * 3)[2:]
    R = int(R, 2)
    if R <= 170:
        ans.append(R)
print(max(ans))
