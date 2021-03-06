## Author: Mohammad Tahir ##

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable

with Device(host='192.168.56.16',username='root',passwd='juniper123') as dev:
    eths = EthPortTable(dev)
    eths.get()
    for port in eths:
        print ("{}: {}".format(port.name, port.oper))

def main():

    with Device(host='192.168.56.16',username='root',passwd='juniper123') as jdev:
        res = jdev.cli('show route 0/0', warning=False)
        res2 = jdev.cli('show ospf nei', warning=False)
        print (res)


if __name__ == "__main__":
    main()
