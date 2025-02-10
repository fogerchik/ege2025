# нашлось
a1 = '12'
a2 = '1234'
print(a1 in a2)
# заменить все вхжления
st = '1231234'
st = st.replace('1', '*')
print(st)

# зменить один раз
st = '1231234'
st = st.replace('1', '*', 1)
print(st)


#фрмирование стоки илроеделенной длины
st='1'*100
print(st)
#умма чисел
summ =0
for i in st:
    summ += int(i)
    #2пособ
summ = sum(map(int,st))
    #3спосоьб
summ = sum(int(i)for i in st)
