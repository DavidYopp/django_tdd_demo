from unittest import skip
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User Goes to homepage and accidentally tries to submit empty list item
        # They press the enter key while on teh empty input textbox

        # The home page refreshes and there is an error message saying that list
        # list items cannot be blank

        # User tries again with text for the tiem and it now works

        # user enters a blank item on'accident' again

        # user gets a warning again for blank items not allowed

        # user can correct this by filling in some textbox
        self.fail('!!Test is failing and you need to continue to write it!!')
