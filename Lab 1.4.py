import ipaddress #ip1 = ipaddress.IPv4Address('192.168.1.0')
import random

network_list = []
for n in range(0, 50):
    net = random.randint(0x0B000000, 0xDF000000)
    mask = random.randint(8, 24)
    ipaddress.IPv4Network((net, mask), strict=False)
    n1 = ipaddress.IPv4Network((net, mask), strict=False)
    network_list.append(n1)

n2 = ipaddress.IPv4Network(int(net), int(mask))
network_list.append(n2)

network_list.sort(reverse=True)
print(network_list)












