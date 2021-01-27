#!/usr/bin/python3
from jnpr.junos import Device
from lxml import etree
import jxmlease
 
username='root'
password='juniper123'
 
dev = Device(host='192.168.56.11', user=username, password=password, normalize=True)

dev.open()
 
rpc = dev.rpc.get_bgp_summary_information()
rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')
dev.close()
 
#print(rpc_xml)
 
xmlparser = jxmlease.Parser()
result = jxmlease.parse(rpc_xml)
 
print(result)

for neighbor in result['bgp-information']['bgp-peer']:
    print('Checking peer with IP address: ' + neighbor['peer-address'])
    print(neighbor['peer-as'])              
    print(neighbor['peer-state'])           
    print(neighbor['elapsed-time'])
