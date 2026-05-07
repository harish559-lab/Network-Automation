from netmiko import ConnectHandler
import time

device = {
    "device_type": "generic_termserver",
    "host": "192.168.180.159",
    "username": "admin",
    "password": "admin",
}

net_connect = ConnectHandler(**device)

print("Entering config mode...")
net_connect.send_command("configure terminal", expect_string=r"\(config.*\)#")

print("Creating VLAN...")
net_connect.send_command("vlan 700", expect_string=r"\(config.*\)#")

print("Naming VLAN...")
net_connect.send_command("name test", expect_string=r"\(config.*\)#")

print("Exiting vlan mode...")
net_connect.send_command("exit", expect_string=r"\(config.*\)#")

print("Exiting config mode...")
net_connect.send_command("exit", expect_string=r"#")

# 🔥 Give device time to stabilize
time.sleep(2)

print("Verifying VLAN...")

output = net_connect.send_command_timing("show vlan")

# Sometimes device needs extra enter
if not output.strip():
    output += net_connect.send_command_timing("\n")

print(output)

