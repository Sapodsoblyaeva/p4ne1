#
import glob
import pprint

files = glob.glob('/Users/sveta/Downloads/config_files/*.log')

network_list = []
for current_file in files:
    with open(current_file) as f:
        for line in f:
            if 'ip address' in line:
                s = 'ip address 192.168.1.0 255.255.255.0'
                network_list.append(s)
                for s1 in s.split()[2:4]:
                    pprint.pprint(s1)










#fname = open('c:\\Users\\sa.podsoblyaeva.JETINF\\Desktop\\seafile\\*.txt')
    #for i in fname:
        #print(i)