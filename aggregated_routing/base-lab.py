from pprint import pprint

import yaml
import decouple
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.utils.config import Config


INVENTORY_FILE = 'inventory.yml'
VARIABLES_FILE = 'vars.yml'

GLOBAL_DEVICE_PARAMS = {
       #  'user': decouple.config('USERNAME'),
       # 'passwd': decouple.config('PASSWORD')

        'user':('root'),
        'passwd':('juniper123')
}



def configure_device(connection_params, variables):
    device_connection = Device(**connection_params)
    device_connection.open()
    # device_connection.facts_refresh()
    facts = device_connection.facts

    hostname = facts['hostname']

    config_variables = variables['devices'][hostname]

    with Config(device_connection, mode='private') as config:
        config.load(template_path='base-template.conf', template_vars=config_variables, format='text', merge=True)
        print("Config diff:")
        config.pdiff()
        config.commit()
        print(f'Configuration was updated successfully on {hostname}')

    device_connection.close()


def do_something(params):
    device_connection = Device(**params)
    device_connection.open()
    # device_connection.facts_refresh()
    facts = device_connection.facts

    # response_xml_element = device_connection.rpc.get_software_information(normalize=True)
    # print(etree.tostring(response_xml_element))
    # pprint(facts)


    print("{0} {1} {0}".format('=' * 37, facts['hostname']))


    device_connection.close()
    # return facts


def read_yaml(file_name=INVENTORY_FILE):
    with open(file_name) as f:
        result = yaml.load(f)
    return result


def get_devices_ip_addresses():
    return read_yaml()['juniper-mx']


def main():
    devices_variables = read_yaml(VARIABLES_FILE)
    juniper_mx_ip_list = get_devices_ip_addresses()
    for juniper_mx_ip in juniper_mx_ip_list:
        params = GLOBAL_DEVICE_PARAMS.copy()
        params['host'] = juniper_mx_ip
        configure_device(params, devices_variables)
    #     do_something(params)
    #     # pprint(facts)


if __name__ == '__main__':
    main()
