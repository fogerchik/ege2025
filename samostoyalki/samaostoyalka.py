#задание 14
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
num = 2 * 729 ** 1021 - 2 * 243 ** 1022 + 81 ** 1023 - 2 * 27 ** 1024 - 1025
print(convert(num,3).count('0'))
#задание 12
for n in range (1 , 1000):
    st = '3' * 15 + '3' * 18 + '1' * n
    while '31' in st or '33' in st or '21'in st:
        if '31' in st:
            st = st.replace('31', '123',1)
        if '33' in st:
            st = st.replace('33', '211',1)
        if '21' in st:
            st = st.replace('21', '1',1)
    summ = sum(int(i) for i in st)
    if summ > 24:
        print(n)
#адание 5
ans = []
for n in range(1, 10_000):
    r = oct(n)[2:]
    if n % 7 == 0:
        r = r + r[-2:]
    else:
        r = r + oct(n % 7 * 7)[2:]
    r = int(r, 8)
    if r < 3000:
        ans.append(r)

print(len(ans))
