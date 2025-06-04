from itertools import permutations
graph ='EB BG GA AB AC CD DF FC FE'.split()
matrix = '246 16 57 15 347 127 356'.split()
print(*range(1,8))
for i in permutations('ABCDEFG'):
    res=[]
    for x ,y in graph:
        res.append(str(i.index(x)+1)in matrix[i.index(y)])
    if all (res):
        print(*i)