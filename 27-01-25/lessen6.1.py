# Цикл while - работает, ПОКА выполняется условие
# Так же как и условный оператор if понимает только True и False

num = 5
cnt = 0
while num > cnt:
    print(cnt, 'Hello')
    cnt += 1

num = 4
while num > 0:
    print('Hello')
    num -= 1

num = 4
while num:
    print('Hello')
    num -= 1