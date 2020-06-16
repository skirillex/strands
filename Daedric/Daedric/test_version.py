import unittest
from constants import *
from version import *


class TestVersion(unittest.TestCase):
    def test_version(self):
        result = Version._VERSION
        got_result = False

        if result != None:
            got_result = True

        self.assertTrue(got_result)
    

class TestVersionIsNot(unittest.TestCase):
    def test_version_is_less(self):
        result = Version.is_less_than_target_version("2.0","3.0")

        self.assertTrue(result)

class TestTuple(unittest.TestCase):
    def test_tuple(self):
        result = Version._as_tuple("2.0")

        self.assertEqual(result, (2, 0))

if __name__ == "__main__":
    unittest.main()