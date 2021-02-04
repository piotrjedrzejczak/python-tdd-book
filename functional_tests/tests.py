from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest, time


class NewVisitor(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retreive_it_later(self):
        # User navigates to the main page of the website.
        self.browser.get(self.live_server_url)

        # The website title suggests it's another boring todo list app.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is welcomed with a window to enter a list item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        # User types in "feed my cat" to a textbox.
        inputbox.send_keys('feed my cat')

        # User submits the item by hitting enter,
        # the list item is now displayed on the website.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: feed my cat')

        # The textbox is still there so user can enter another item.
        self.fail('Finish the test bud!')

        # When user added his first item do the list it's now preserved
        # under a unique URL.
