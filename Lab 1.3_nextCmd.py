from pysnmp.hlapi import *

obj_ver = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")

result = nextCmd(SnmpEngine(),
				 CommunityData("public", mpModel=0),
				 UdpTransportTarget(("10.31.70.209", 161)),
				 ContextData(),
				 ObjectType(obj_ver),
				 lexicographicMode=False)

def interfaces():
	for received_data in result:
		for x in received_data[3]:
			yield x

for i in interfaces():
	print(i)
