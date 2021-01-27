# Author: Mohammad Tahir @CloudKod.com
from jnpr.junos.utils.start_shell import StartShell
from jnpr.junos import Device
dev=Device(host='192.168.56.11', user='root', password='juniper123')
ss = StartShell(dev)
with StartShell(dev) as ss:    
    cmd_1 = ss.run('cli -c "show route 10.10.4.0/22 exact detail"', timeout=20)[1]
    cmd_2 = ss.run('cli -c "show route 10.10.4.0/22 exact"')[1]
    # run a Junos CLI command from shell
    # cmd_3 = ss.run('cli -c "show version | no-more"')[1]
print(cmd_1)
print(cmd_2)
# print(cmd_3)
