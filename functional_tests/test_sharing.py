from selenium import webdriver
from .base import FunctionalTest


def quit_if_possible(browser):
    try: browser.quit()
    except: pass


class SharingTest(FunctionalTest):

    def test_can_share_list_with_another_user(self):
        # example@user.com is a logged in user
        self.create_pre_authenticated_session('example@user.com')
        user_browser = self.browser
        self.addCleanup(lambda: quit_if_possible(user_browser))

        # a friend of example user name example2 is also on the site
        user2_browser = webdriver.Firefox()
        self.addCleanup(lambda: quit_if_possible(user2_browser))
        self.browser = user2_browser
        self.create_pre_authenticated_session('example2@user.com')

        # the first example user goes to the homepage and starts a list
        self.browser = user_browser
        self.browser.get(self.live_server_url)
        self.add_list_item('Get help')

        # the user notices a "Share this list" option
        share_box = self.browser.find_element_by_css_selector(
            'input[name=sharee]'
        )
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )
