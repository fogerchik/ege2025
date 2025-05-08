from ipaddress import ip_network, ip_address

net = ip_network('248.112.{a}.35/255.255.255.240')
max_sum_1 = 0
for i in net:
    i = f'{int(i):032b}'
    max_sum_1 = max(max_sum_1, i.count('1'))
print(max_sum_1)