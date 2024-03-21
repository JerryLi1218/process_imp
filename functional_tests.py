from selenium import webdriver
import unittest

class New_visitor_test(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''
        some one hear that there is an online application for To-Do list
        he is going to take a look 
        '''
        self.browser.get('http://localhost:8000')

        # He notes that there is a "To-Do" in the home page
        self.assertIn('To-Do', self.browser.title), "browser title was:" + self.browser.title
        self.fail('Finish the test')

        # The application has a text entry field for to-do item

        # He typed "Buy Flower" in the text box (so romantic~)
        
        # He visited the URL and found that his list was still there
        
        # He left satisfied

if __name__ == '__main__':
    unittest.main()
