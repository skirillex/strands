import mainPage
import unittest

# for performance test
class MyTestCase(unittest.TestCase):

    def setUp(self):
        mainPage.app.testing = True
        self.app = mainPage.app.test_client()



    # looks to see if the home page is reachable
    def test_home(self):
        result = self.app.get('/')
        got_page = False

        if result != None:
            got_page = True


        self.assertTrue(got_page)
    
