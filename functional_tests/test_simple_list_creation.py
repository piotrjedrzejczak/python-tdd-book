from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retreive_it_later(self):
        # User navigates to the main page of the website.
        self.browser.get(self.live_server_url)

        # The website title suggests it's another boring todo list app.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is welcomed with a window to enter a list item.
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        # User types in "feed my cat" to a textbox.
        inputbox.send_keys('feed my cat')

        # User submits the item by hitting enter,
        # the list item is now displayed on the website.
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: feed my cat')

    def test_multiple_users_can_start_lists_at_different_urls(self):

        # User creates his own list.
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('feed my cat')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: feed my cat')

        # When new list is created a unique URL should be generated.
        personal_url = self.browser.current_url
        self.assertRegex(personal_url, '/lists/.+')

        # New users comes in and creates a list.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # User does not find the previous users list.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('feed my cat', page_text)
        
        # Now the users creates his own list.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('pet my doggo')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: pet my doggo')

        # He gets his own URL.
        next_personal_url = self.browser.current_url
        self.assertRegex(next_personal_url, '/lists/.+')
        self.assertNotEqual(personal_url, next_personal_url)

        # No trace of previous users list items.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('feed my cat', page_text)
