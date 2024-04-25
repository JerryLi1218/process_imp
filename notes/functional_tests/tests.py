from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest, time
from django.test import LiveServerTestCase

class New_visitor_test(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''
        some one hear that there is an online application for To-Do list
        he is going to take a look 
        '''
        self.browser.get(self.live_server_url)

        # He notes that there is a "To-Do" in the home page
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # The application has a text entry field for to-do item
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He typed "Buy Flower" in the text box (so romantic~)
        inputbox.send_keys('Buy flowers')

        # He pushed the buttum 'Return', and the browser refresh
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy flowers')

        # The application has a text entry field for to-do item
        # He typed "Give a gift to Lisi" in the text box
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Give a gift to Lisi')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # He pushed the buttum 'Return', and the browser refresh
        self.check_for_row_in_list_table('1: Buy flowers')
        self.check_for_row_in_list_table('2: Give a gift to Lisi')

        # He visited the URL and found that his list was still there
        self.fail('Finish the test.')

        # He left satisfied
