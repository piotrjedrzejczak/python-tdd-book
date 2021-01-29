from selenium import webdriver
import unittest


class NewVisitor(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):
        # User navigates to the main page of the website.
        self.browser.get('http://localhost:8000')

        # The website title suggests it's another boring todo list app.
        self.assertIn('To-Do', self.browser.title)

        # This will just fail and remind you to finish this test!
        self.fail('Finish the test buddy!')

        # User is welcomed with a window to enter a list item.

        # User types in "feed my cat" to a textbox.

        # User submits the item by hitting enter,
        # the list item is now displayed on the website.

        # The textbox is still there so user can enter another item.

        # When user added his first item do the list it's now preserved
        # under a unique URL.

if __name__ == '__main__':
    unittest.main()
