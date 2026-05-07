from pyats import aetest
from netmiko import ConnectHandler

class VLANTest(aetest.Testcase):

    @aetest.test
    def verify_vlan(self):

        device = {
            "device_type": "linux",
            "host": "192.168.180.131",
            "username": "admin",
            "password": "admin",
        }

        net_connect = ConnectHandler(**device)

        output = net_connect.send_command_timing(
            "show vlan",
            strip_prompt=False,
            strip_command=False
        )

        print(output)

        if "700" in output:
            self.passed("VLAN 700 exists")
        else:
            self.failed("VLAN 700 NOT found")

        net_connect.disconnect()

if __name__ == "__main__":
    aetest.main()
