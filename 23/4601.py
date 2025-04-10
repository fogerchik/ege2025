def f(current, petuxend):
    if current == petuxend:
        return 1
    if current < petuxend:
        return 0
    return f(current - 1, petuxend) + f(current // 2, petuxend)


print(f(30, 12) * f(12, 1))
