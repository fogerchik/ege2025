#13)
from ipaddress import ip_network
net = ip_network('214.187.224.0/255.255.224.0')
cnt = 0
for i in net:
    i = f'{int(i):32b}'
    if i.count('1') %6 != 0 and i[28:] == "1000":
        cnt += 1
print(cnt)

from ipaddress import ip_network

for a in range(256):
    net = ip_network(f'248.112.{a}.35/255.255.255.240', False)
    cnt = 0
    for i in net:
        i = f'{int(i):32b}'
        if i[:16].count('0') <= i[16:].count('0'):
            cnt += 1
    if cnt == net.num_addresses:
            print(a)

def f(cur, end):
    if cur == end: return 1
    if cur > end or cur == 21: return 0
    return f(cur + 2, end) + f( cur + 3, end)+ f(cur * 2,end)

print(f(7,14)* f(14,32))

