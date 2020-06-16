import unittest
from constants import *



class TestTAG(unittest.TestCase):
    def test_tag(self):
        result = TAG

        self.assertEqual(result, "Daedric")

class TestVersion(unittest.TestCase):
    def test_version_num(self):
        result = VERSION

        flag = False
        if (result != None):
            flag = True
        
        self.assertTrue(flag)

if __name__ == "__main__":
    unittest.main()