from unittest import skip
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')


    def test_cannot_add_empty_list_items(self):
        # User Goes to homepage and accidentally tries to submit empty list item
        # They press the enter key while on the empty input textbox
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        #The browser intercepts the request, and does not load the list page_text
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))

        #user starts typing some text for the new item and the error disappears
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
        ))

        # User can submit this successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # user enters a blank item on 'accident' again
        self.get_item_input_box().send_keys(Keys.ENTER)

        # user gets a browser blank input error warning again
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))

        # user can correct this by filling in some textbox
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')


    def test_cannot_add_duplicate_items(self):
        #user goes to home page and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy graphics card')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy graphics card')

        #user accidentally enter a duplicate item
        self.get_item_input_box().send_keys('Buy graphics card')
        self.get_item_input_box().send_keys(Keys.ENTER)

        #user gets an duplicate item error message
        self.wait_for(lambda: self.assertEqual(
            self.get_error_element().text,
            "You've already got this item in your list"
        ))


    def test_error_messages_are_cleared_on_input(self):
        # user starts a list that causes a validation errors
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Seagulls Stop it now')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Seagulls Stop it now')
        self.get_item_input_box().send_keys('Seagulls Stop it now')
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertTrue(
            self.get_error_element().is_displayed()
        ))

        # user starts typing in the input box again to clear the error error_messages
        self.get_item_input_box().send_keys('a')

        #user sees that the error message has gone away
        self.wait_for(lambda: self.assertFalse(
            self.get_error_element().is_displayed()
        ))
