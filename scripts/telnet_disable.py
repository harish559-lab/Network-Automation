from netmiko import ConnectHandler

device = {
    "device_type": "linux",
    "host": "192.168.180.178",
    "username": "admin",
    "password": "admin",
}

connection = ConnectHandler(**device)

commands = [
    "configure terminal",
    "no aaa authentication login telnet local",
    "end",
    "copy running-config startup-config"
]

for cmd in commands:
    output = connection.send_command(
        cmd,
        expect_string=r'[#\$]'
    )
    print(output)

connection.disconnect()
