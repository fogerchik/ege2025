from itertools import product

cnt = 0
for i in product('IGROK', repeat=5):
    i = ''.join(i)
    if len(i) == len(set(i)):
        # Проверка, что строка не начинается на какой-то символ
        if i[0] != 'K' and 'ROK' not in i:
            cnt += 1
print(cnt)