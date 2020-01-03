from selenium import webdriver
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
        self.fail('Finish the Test!')

        # User is invited to enter a todo item

        # user types in buy peacock feathers into the textbox

        # user presses the enter key, the page updates, and the page now lists:
        # '1: buy peacock feathers' In the todo list items

        # textbox to enter another item is still on teh page so user enters:
        # use the feathers to make a fly for fly fishing

        # page updates and the todo item list now shows both items

        # user wonders if the site will remember her list and sees that the site generated
        # a unique url for them --there is explanatory text that reflects this

        # user visits the unique url and their todo list is there

        # user stops using site and goes to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
