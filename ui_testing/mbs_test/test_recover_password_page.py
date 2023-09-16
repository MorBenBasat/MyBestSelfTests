import unittest
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage


class TestRecoverPage(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver()  # Initialize the WebDriver
        self.helpers = HelpersMbs(self.driver)  # Create an instance of the LoginPage clas
        self.login_page = LoginPage(self.driver)  # Create an instance of the LoginPage class

    def test_only_send_email(self):
        pass

    def test_verify_email_in_gmail(self):
        pass

    def test_not_valid_email(self):
        pass

    def test_not_exist_email(self):
        pass
