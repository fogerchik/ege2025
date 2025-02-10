for n in range(4, 10_000):
    st = '5' + '2' * n
    while '72' in st or "522" in st or '2222' in st:
        if '72' in st:
            st = st.replace('72', '2', 1)
        if '522' in st:
            st = st.replace('522','27',1)
        if '2222' in st:
            st = st.replace('2222','5', 1)

    summ = sum(int(i)for i in st
    if summ == 63:

#или это тоэе самое
for n in range(4, 10_000):
    st = '5' + '2' * n
    while '72' in st or "522" in st or '2222' in st:
        st = st.replace('72', '2', 1)
        st = st.replace('522','27',1)
        st = st.replace('2222','5', 1)