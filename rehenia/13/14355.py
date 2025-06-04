from ipaddress import ip_network, ip_address

for mask in range (16,25):
    net = ip_network(f'127.63.67.1/{mask}', False)
    cnt = 0
    for i in net:
        i = f'{int(i):32b}'
        if i[:16].count('1') >= i[16:].count('1'):
            cnt += 1
    if cnt == net.num_addresses:
        print(mask, net.netmask)