from ipaddress import ip_network, ip_address

ip = ip_address('143.131.211.37')
for mask in range(10, 31):
    net = ip_network(f'{ip}/{mask}',False)
    cnt = 0
    if ip in net.hosts():
        for i in net:
            i = f'{int(i):032b}'
            if i.count('1') ==10:
                cnt +=1
    if cnt>=15:
        print(mask)