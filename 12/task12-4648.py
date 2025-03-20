st = '2' * 55 + '3' * 44 + '1' * 33
while "222" in st or "333" in st or  "111" in st:
    if '222' in st:
        st = st.replace('222','11',1)
        if '222' in st:
            st = st[::-1].replace('222', '11', 1)[::-1]
    elif '111' in st:
            st = st.replace('111', '3', 1)
    else:
            st = st.replace('333', '1', 1)
print(st)
