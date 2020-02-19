import time
from selenium import webdriver
from .base import FunctionalTest
from .list_page import ListPage
from .my_lists_page import MyListsPage


def quit_if_possible(browser):
    try:
        time.sleep(5)
        browser.quit()
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
        list_page = ListPage(self).add_list_item('Get help')

        # the user notices a "Share this list" option
        share_box = list_page.get_share_box()
        self.assertEqual(
            share_box.get_attribute('placeholder'),
            'your-friend@example.com'
        )

        # User shares their list
        # page updates to say that its shared with example2@user.com
        list_page.share_list_with('example2@user.com')

        # example2@suer.com goes to the lists page
        self.browser = user2_browser
        MyListsPage(self).go_to_my_lists_page()

        # example2@user.com sees example@user's list in list there!
        self.browser.find_element_by_link_text('Get help').click()

        # example2@user.com can see that the new list is example@user.com's list
        self.wait_for(lambda: self.assertEqual(
            list_page.get_list_owner(),
            'example@user.com'
        ))

        # example2@user.com adds an item to the shared list
        list_page.add_list_item('Hello example!')

        # when example refreshes the page they see the 'Hello' addtion from user 'example2'
        self.browser = user_browser
        self.browser.refresh()
        list_page.wait_for_row_in_list_table('Hello example!', 2)
