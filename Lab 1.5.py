#
import glob

files = glob.glob('c:\\Users\\sa.podsoblyaeva.JETINF\\Desktop\\seafile\\*.log')

network_list = []
for current_file in files:
    with open(current_file) as f:
        for line in f:
            if 'ip address' in line:
                s = 'ip address 192.168.1.0 255.255.255.0'
                network_list.append(s)
                for s1 in s.split()[2:4]:
                    print(s1, end=' ')










#fname = open('c:\\Users\\sa.podsoblyaeva.JETINF\\Desktop\\seafile\\*.txt')
    #for i in fname:
        #print(i)