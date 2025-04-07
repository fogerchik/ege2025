from sys import setrecursionlimit
def f(n):
    if n < 11:
        return n
    if n >= 11:
        return n +f(n-1)
setrecursionlimit(1242356)
print(f(2024) - f(2021))

2

from functools import lru_cache
@ lru_cache(None)
def f(n):
    if n < 11:
        return n
    if n >= 11:
        return n +f(n-1)
for i in range(10,2025):
    f(i)
print(f(2024) - f(2021))


3


2024 = 2023 + 2022 + f(2024) - f(2021)
