import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='./geckodriver')

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)

        self.fail('FINISH')