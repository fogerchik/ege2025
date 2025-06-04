import ipaddress
from ipaddress import ip_network
net=ip_network('172.16.128.0/18')
cnt=0
for i in net:
    i=f'{int(i):032b}'
    if i.count('1') %2 != 2:
        cnt +=1
print(cnt)

