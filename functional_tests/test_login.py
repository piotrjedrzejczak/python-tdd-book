from django.core import mail
from selenium.webdriver.common.keys import Keys
import re

from .base import FunctionalTest

TEST_MAIL = 'cor7zzzz@example.com'
SUBJECT = 'Your login link for Superlists'


class LoginTest(FunctionalTest):

    def test_can_get_email_link_to_log_in(self):
        # User vists the website and notices login form.
        # Using that form user logs in.
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('email').send_keys(TEST_MAIL)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

        # A message appears telling the user that an email has been sent to her.
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))

        # User checks his mailbox.
        email = mail.outbox[0]
        self.assertIn(TEST_MAIL, email.to)
        self.assertEqual(email.subject, SUBJECT)

        # The email has a URL inside.
        self.assertIn('Use this link to log in', email.body)
        url_search = re.search(r'http://.+/.+$', email.body)
        if not url_search:
            self.fail(f'Could not find url in email body.\n{email.body}')
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # User navigates to the link.
        self.browser.get(url)

        # User is now logged in.
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Log out')
        )
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(TEST_MAIL, navbar.text)
