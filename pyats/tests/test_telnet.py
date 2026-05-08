from pyats import aetest
import telnetlib

HOST = "192.168.180.178"

class TelnetTest(aetest.Testcase):

    @aetest.test
    def verify_telnet_enabled(self):

        try:
            tn = telnetlib.Telnet(HOST, 23, timeout=5)
            tn.close()

            self.passed("Telnet connection successful")

        except Exception as e:
            self.failed(f"Telnet failed: {str(e)}")
