from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User tries to add an empty list item by hitting enter on the home page.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Page refreshes, and there is an error message saying
        # that you cannot add empty list items.
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:invalid'))

        # User tries again with some text.
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:valid'))

        # Submits the form and it works.
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Tries to submit the empty form again.
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Receives a simmilar warning message from the webpage.
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:invalid'))

        # She can correct it by filling some text in.
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_element_by_css_selector('#id_text:valid'))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

    
    def test_cannot_add_duplicate_items(self):
        # User goes to the home page and starts a new list.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys('Buy plainer')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy plainer')

        # User tries to enter the same item again.
        self.get_item_input_box().send_keys('Buy plainer')
        self.get_item_input_box().send_keys(Keys.ENTER)
        
        # User sees an error message.
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You've already got this in your list"
        ))
