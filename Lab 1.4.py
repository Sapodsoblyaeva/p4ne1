import ipaddress #ip1 = ipaddress.IPv4Address('192.168.1.0')
import random

network_list = []
for n in range(0, 50):
    net = int(random.randint(0x0B000000, 0xDF000000))
    mask = int(random.randint(8, 24))
    ipaddress.IPv4Network((net, mask), strict=False)
    n1 = ipaddress.IPv4Network((net, mask), strict=False)
    network_list.append(n1)

for x in network_list:
    network_list.sort()
    print(x)













