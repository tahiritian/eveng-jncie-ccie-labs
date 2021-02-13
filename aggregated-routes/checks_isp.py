## Author: Mohammad Tahir ##

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable

with Device(host='192.168.56.15',username='root',passwd='juniper123') as dev:

    with Device(host='192.168.56.15',username='root',passwd='juniper123') as jdev:
        res = jdev.cli('show route protocol bgp', warning=False)
        print (res)

