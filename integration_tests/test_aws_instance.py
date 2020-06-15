import unittest
import re
import requests

class TestIfInstanceIsOnline(unittest.TestCase):

    def test_EC2_instance(self):
        ipaddr_file = open("../terraform/ip_address")

        ip_addresses = []

        for line in ipaddr_file:
            ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)


            if len(ip_candidates) != 0:
                ip_addresses.append(ip_candidates[0])


        r = []
        for n in range(0, len(ip_addresses)):
            url = "http://"+ip_addresses[n - 1]

            r.append(requests.get(url = url))


        # if any IP's are not reachable then fail test
        test_pass_flag = True
        for x in r:
            if x.ok != True:
                test_pass_flag = False


        self.assertTrue(test_pass_flag)