from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User hears about todo list app and gose to check out its homepage at localhost
        self.browser.get(self.live_server_url)

        # User notices the page title and header mentions todo lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
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
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # textbox to enter another item is still on teh page so user enters:
        # use the feathers to make a fly for fly fishing
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # page updates and the todo item list now shows both items
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # user wonders if the site will remember her list and sees that the site generated
        # a unique url for them --there is explanatory text that reflects this
        self.fail('Everything else passed! Success!! now ... FINISH THE TEST!!')

        # user visits the unique url and their todo list is there

        # user stops using site and goes to sleep

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')
