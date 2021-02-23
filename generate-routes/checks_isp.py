## Author: Mohammad Tahir ##

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable

with Device(host='192.168.56.15',username='root',passwd='juniper123') as dev:

    with Device(host='192.168.56.15',username='root',passwd='juniper123') as jdev:
        res = jdev.cli('show  bgp summ', warning=False)
        res4 = jdev.cli('show interfaces ge-0/0/5 | match Up', warning=False)
        res1 = jdev.cli('show ospf neighbor', warning=False)
        res2 = jdev.cli('show route 0/0 exact detail', warning=False)
        res3 = jdev.cli('show route 10.10.4.0/22', warning=False)
        print (res)
        print (res1)
        print (res2)
        print (res3)
        print (res4)
