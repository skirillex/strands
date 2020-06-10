import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        print("if you're seeing this then that means \ncircleCI pulled this code from github \nand ran the test suite against this app")
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()