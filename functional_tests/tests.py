from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
import os


MAX_WAIT_TIME = 10


class NewVisitor(StaticLiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()

    def test_layout_and_styling(self):
        # User visits the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # User notices the inputbox is centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # User starts adding list items
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        # User notices the inputbox is centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:  
            try:
                table = self.browser.find_element_by_id('id_list_table')  
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT_TIME:  
                    raise e  
                time.sleep(0.5)  

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
        self.wait_for_row_in_list_table('1: feed my cat')

    
    def test_multiple_users_can_start_lists_at_different_urls(self):

        # User creates his own list.
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('feed my cat')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: feed my cat')

        # When new list is created a unique URL should be generated.
        personal_url = self.browser.current_url
        self.assertRegex(personal_url, '/lists/.+')

        # New users comes in and creates a list.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # User does not find the previous users list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('feed my cat', page_text)
        
        # Now the users creates his own list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('pet my doggo')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: pet my doggo')

        # He gets his own URL
        next_personal_url = self.browser.current_url
        self.assertRegex(next_personal_url, '/lists/.+')
        self.assertNotEqual(personal_url, next_personal_url)

        # No trace of previous users list items
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('feed my cat', page_text)