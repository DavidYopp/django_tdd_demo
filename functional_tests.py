from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User hears about todo list app and gose to check out its homepage at localhost
        self.browser.get('http://localhost:8000')

        # User notices the page title and header mentions todo lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').textbox
        self.assertIn('To-Do', header_text)

        # User is invited to enter a todo item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
        inputbox.get_attribute('placeholder'),
        'Enter a to-do item'
        )

        # user types in buy peacock feathers into the textbox
        inputbox.send_keys('Buy peacock feathers')

        # user presses the enter key, the page updates, and the page now lists:
        # '1: buy peacock feathers' In the todo list items
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # textbox to enter another item is still on teh page so user enters:
        # use the feathers to make a fly for fly fishing
        self.fail('Everything else passed! Success!! now ... FINISH THE TEST!!')

        # page updates and the todo item list now shows both items

        # user wonders if the site will remember her list and sees that the site generated
        # a unique url for them --there is explanatory text that reflects this

        # user visits the unique url and their todo list is there

        # user stops using site and goes to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
