from netmiko import ConnectHandler
import time

switch = {
    "device_type": "terminal_server",
    "host": "192.168.180.178",
    "username": "admin",
    "password": "admin",
}

print("\nConnecting to switch...\n")

connection = ConnectHandler(**switch)

print("Connected successfully\n")

# Disable pagination
connection.send_command("terminal length 0")

# Configure hostname
print("Configuring hostname...\n")

connection.write_channel("configure terminal\n")
time.sleep(1)

output = connection.read_channel()
print(output)

connection.write_channel("hostname Hfcl-Switch\n")
time.sleep(1)

output = connection.read_channel()
print(output)

connection.write_channel("exit\n")
time.sleep(1)

output = connection.read_channel()
print(output)

# Verify hostname
print("\nVerifying hostname...\n")

verify = connection.send_command("show running-config")

if "hostname Hfcl-Switch" in verify:
    print("Hostname configured successfully\n")
else:
    print("Hostname configuration FAILED\n")

# Test invalid hostname
print("Testing invalid hostname...\n")

invalid_hostname = "A" * 256

connection.write_channel("configure terminal\n")
time.sleep(1)

print(connection.read_channel())

connection.write_channel(f"hostname {invalid_hostname}\n")
time.sleep(2)

invalid_output = connection.read_channel()

print(invalid_output)

connection.write_channel("exit\n")
time.sleep(1)

print(connection.read_channel())

# Verify invalid hostname not applied
verify_invalid = connection.send_command("show running-config")

if invalid_hostname in verify_invalid:
    print("Invalid hostname applied - FAIL\n")
else:
    print("Invalid hostname rejected correctly - PASS\n")

# Save configuration
print("Saving configuration...\n")

save_output = connection.send_command_timing(
    "copy running-config startup-config",
    strip_prompt=False,
    strip_command=False
)

print(save_output)

# Handle confirmation prompt if device asks
if "confirm" in save_output.lower():
    save_output += connection.send_command_timing(
        "\n",
        strip_prompt=False,
        strip_command=False
    )

print(save_output)

time.sleep(5)

# Reload switch
print("Reloading switch...\n")

reload_output = connection.send_command_timing(
    "reload warm",
    strip_prompt=False,
    strip_command=False
)

print(reload_output)

# Handle reload confirmation if prompted
if "confirm" in reload_output.lower():
    connection.send_command_timing("\n")

connection.disconnect()

print("Waiting for switch reboot...\n")

time.sleep(120)

# Reconnect after reboot
print("Reconnecting after reboot...\n")

reconnect = ConnectHandler(**switch)

final_output = reconnect.send_command("show running-config")

if "hostname Hfcl-Switch" in final_output:
    print("Hostname persisted after reboot - PASS\n")
else:
    print("Hostname missing after reboot - FAIL\n")

reconnect.disconnect()

print("Testcase completed successfully.\n")
