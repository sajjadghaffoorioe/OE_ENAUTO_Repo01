from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

ipaddresses = ["10.10.10.10", "10.10.10.11"]

devices = [
    {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "admin",
        "password": password,
    }
    for ip in ipaddresses
]

for device in devices:
    print(f'Connecting to the device: {device["host"]}')

    with ConnectHandler(**device) as net_connect:
        intf_brief = net_connect.send_command(
            "show ip interface brief"
        )
        facts = net_connect.send_command("show version")

    print(intf_brief)
    print(facts)
