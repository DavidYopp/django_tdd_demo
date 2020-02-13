import time
from django.conf import settings
from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session


class MyListsTest(FunctionalTest) :

    def create_pre_authenticated_session(self, email):
        if self.staging_server:
            session_key = create_session_on_server(self.staging_server, email)
        else:
            session_key = create_pre_authenticated_session(email)
        ## to set a cookie we need to visit the domain
        ## 404 pages load the quickest
        self.browser.get(self.live_server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/',
        ))


    def test_logged_in_users_lists_are_saved_as_my_lists(self):

        #user 'example' is a logged in user
        self.create_pre_authenticated_session('example@gmail.com')

        #user goes to homepage and starts a list
        self.browser.get(self.live_server_url)
        self.add_list_item('Reticulating splines')
        self.add_list_item('articulating splines')
        first_list_url = self.browser.current_url

        #user notices a 'My lists' link for the first time
        self.browser.find_element_by_link_text('My lists').click()

        #user notices their list is there named according to the first list item
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Reticulating splines')
        )
        self.browser.find_element_by_link_text('Reticulating splines').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        #user starts another list out of curiosity
        self.browser.get(self.live_server_url)
        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url

        #under 'My lists' the users list appears
        self.browser.find_element_by_link_text('My lists').click()
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Click cows')
        )
        self.browser.find_element_by_link_text('Click cows').click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        #user logs out. the 'My lists' option disappears
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_elements_by_link_text('My lists'),
            []
        ))
        self.fail()
