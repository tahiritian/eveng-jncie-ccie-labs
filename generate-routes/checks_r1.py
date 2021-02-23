## Author: Mohammad Tahir ##

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable

with Device(host='192.168.56.11',username='root',passwd='juniper123') as dev:
    eths = EthPortTable(dev)
    eths.get()
    for port in eths:
        print ("{}: {}".format(port.name, port.oper))

def main():

    with Device(host='192.168.56.11',username='root',passwd='juniper123') as jdev:
        res = jdev.cli('show route', warning=False)
        res1 = jdev.cli('show bgp summary', warning=False)
        res2 = jdev.cli('show ospf nei', warning=False)
        res3 = jdev.cli('show route 10.10.4.0/22 exact detail', warning=False)
        print (res)
        print (res1)
        print (res2)
        print (res3)


if __name__ == "__main__":
    main()
