import mainPage
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        mainPage.app.testing = True
        self.app = mainPage.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        got_page = False

        if result != None:
            got_page = True

        #test_page_string = self.app.get('/John')
        #print(test_page_string)
        #self.assertEqual(result, "<Response streamed [200 OK]>")

        self.assertTrue(got_page)
    