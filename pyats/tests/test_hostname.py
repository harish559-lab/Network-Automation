from pyats import aetest
from netmiko import ConnectHandler

class HostnameTest(aetest.Testcase):

    @aetest.test
    def verify_hostname(self):

        device = {
            'device_type': 'linux',
            'host': '192.168.180.178',
            'username': 'admin',
            'password': 'admin',
        }

        connection = ConnectHandler(**device)

        output = connection.send_command("show running-config | include hostname")

        print(output)

        expected_hostname = "HFCL-Switch"

        if expected_hostname in output:
            self.passed(f"Hostname {expected_hostname} exists")
        else:
            self.failed(f"Hostname {expected_hostname} NOT found")

        connection.disconnect()
