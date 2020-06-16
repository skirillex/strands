import unittest
import re
import requests

class TestIfAPIAbout(unittest.TestCase):

    def test_about_page(self):
        ipaddr_file = open("../terraform/ip_address")

        ip_addresses = []

        # obtain ip addresses from ansible file
        for line in ipaddr_file:
            ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)


            if len(ip_candidates) != 0:
                ip_addresses.append(ip_candidates[0])



        # check that a site is deployed at all addresses in file
        # check the about page
        test_pass_flag = True
        try:
            for n in range(0, len(ip_addresses)):
                url = "http://"+ip_addresses[n - 1]+"/about"
                html_content = requests.get(url, verify=False, timeout=4).text
                #print(html_content)

        except:
            test_pass_flag = False
        


        self.assertTrue(test_pass_flag)

class TestIfAPIExtra(unittest.TestCase):

    def test_extra_page(self):
            ipaddr_file = open("../terraform/ip_address")

            ip_addresses = []

            # obtain ip addresses from ansible file
            for line in ipaddr_file:
                ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)


                if len(ip_candidates) != 0:
                    ip_addresses.append(ip_candidates[0])



            # check that a site is deployed at all addresses in file
            # check the extra page
            test_pass_flag = True
            try:
                for n in range(0, len(ip_addresses)):
                    url = "http://"+ip_addresses[n - 1]+"/John"
                    html_content = requests.get(url, verify=False, timeout=4).text
                    #print(html_content)

            except:
                test_pass_flag = False
            


            self.assertTrue(test_pass_flag)

class TestIfAPIHome(unittest.TestCase):
    def test_home_page(self):
            ipaddr_file = open("../terraform/ip_address")

            ip_addresses = []

            # obtain ip addresses from ansible file
            for line in ipaddr_file:
                ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)


                if len(ip_candidates) != 0:
                    ip_addresses.append(ip_candidates[0])



            # check that a site is deployed at all addresses in file
            # check the about page
            test_pass_flag = True
            try:
                for n in range(0, len(ip_addresses)):
                    url = "http://"+ip_addresses[n - 1]+"/"
                    html_content = requests.get(url, verify=False, timeout=4).text
                    #print(html_content)

            except:
                test_pass_flag = False
            


            self.assertTrue(test_pass_flag)