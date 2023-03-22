from pysnmp.hlapi import *

obj_ver = ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)

result = getCmd(SnmpEngine(), CommunityData("public", mpModel=0), UdpTransportTarget(("10.31.70.209", 161)), ContextData(), ObjectType(obj_ver))

for received_data in result:
	for x in received_data[3]:
		print(x)