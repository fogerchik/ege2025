import itertools
from itertools import product, repeat

alph = sorted('январь')
cnt = 0
for i in product( alph,repeat=5):
    i = ''.join(i)
    cnt+=1
    if i[0] != 'я' and i.count('ь') <= 1 and i.count('яя')==0:
        print(cnt,i)
