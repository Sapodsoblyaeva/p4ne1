
import re
import glob
import ipaddress

files = glob.glob('c:\\Users\\sa.podsoblyaeva.JETINF\\Desktop\\seafile\\*.log')

for current_file in files:
    with open(current_file) as f:
        for line in f:
            if "ip address" in line:
                print(line)

res = re.match('^ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})$', ' ip address 192.168.1.1 255.255.255.0')


ip_int = res.group(1) + "/" + res.group(2)
ipaddress.IPv4Interface(ip_int)




