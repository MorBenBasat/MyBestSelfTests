import unittest
import pytest

from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from pages.RecoverPasswordPage import RecoverPasswordPage
from test_users.recover_password_page_users import ValidEmail, InvalidEmailType, NoEmail


class TestRecoverPage(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver()  # Initialize the WebDriver
        self.helpers = HelpersMbs(self.driver)  # Create an instance of the LoginPage clas
        self.login_page = LoginPage(self.driver)  # Create an instance of the LoginPage class
        self.recover_password = RecoverPasswordPage(self.driver)

    @pytest.mark.test77
    def test_success_navigation_recover_password_page(self):
        self.recover_password.navigation_to_recover_password_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.recover_password, print("Recover Password Page Open"))

    @pytest.mark.test78
    def test_success_sending_email(self):
        self.recover_password.navigation_to_recover_password_page()
        self.recover_password.send_email(ValidEmail)
        # need to add asserttion

    def test_verirfy_mandatory_email_field(self):
        pass

    def test_verify_email_in_gmail(self):
        pass

    @pytest.mark.test79
    def test_not_valid_email(self):
        self.recover_password.navigation_to_recover_password_page()
        result_message = self.recover_password.invalid_email_login(InvalidEmailType)
        expected_message = 'נא להזין מייל חוקי'
        self.assertEqual(result_message, expected_message, "Expected message does not match actual message.")

    @pytest.mark.test80
    def test_not_exist_email(self):
        self.recover_password.navigation_to_recover_password_page()
        self.recover_password.send_email(NoEmail)

    def test_click_register_btn(self):
        self.recover_password.click_register_btn()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.register, print('נפתח דף הרשמה למערכת'))

    def test_click_login_btn(self):
        self.recover_password.click_login_btn()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, print("נפתח דף כניסה למערכת"))
