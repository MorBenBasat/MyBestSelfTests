import unittest
import pytest

from helpers.AlertsAndStrings import DisableBtn, MandatoryFieldText
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from locators import RecoverPasswordPageLocators
from locators.RecoverPasswordPageLocators import RecoverPasswordPageLocators
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from pages.RecoverPasswordPage import RecoverPasswordPage
from test_users.recover_password_page_users import ValidEmail, InvalidEmailType, NoEmail


class TestRecoverPage(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.recover_password = RecoverPasswordPage(self.driver)

    @pytest.mark.test77
    def test_success_navigation_recover_password_page(self):
        self.recover_password.navigation_to_recover_password_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.recover_password, print("Recover Password Page Open"))

    @pytest.mark.test78
    def test_success_sending_email(self):
        self.recover_password.navigation_to_recover_password_page()
        self.recover_password.fill_send_email(ValidEmail)

    def test_verify_mandatory_email_field(self):
        self.recover_password.navigation_to_recover_password_page()
        result_text = self.recover_password.mandatory_email_text(NoEmail)
        expected_text = MandatoryFieldText.alert
        self.assertEqual(result_text, expected_text, print(MandatoryFieldText.alert))

    def test_verify_email_valid(self):
        pass
        #pass
    @pytest.mark.test79
    def test_not_valid_email(self):
        self.recover_password.navigation_to_recover_password_page()
        error_message = self.recover_password.invalid_email_login(InvalidEmailType)
        expected_message = 'נא להזין מייל חוקי'
        self.assertEqual(error_message, expected_message)

    @pytest.mark.test80
    def test_not_exist_email(self):
        self.recover_password.navigation_to_recover_password_page()
        email_btn_disable = HelpersMbs.is_disabled(self.driver, RecoverPasswordPageLocators.CONFIRM_BTN)
        self.recover_password.fill_email_without_click_btn(InvalidEmailType)
        self.assertEqual(email_btn_disable, True, print(DisableBtn.my_string))
        HelpersMbs.delay(2)
        self.driver.quit()

    def test_click_register_btn(self):
        self.recover_password.click_register_btn()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.register, print('נפתח דף הרשמה למערכת'))

    def test_click_login_btn(self):
        self.recover_password.click_login_btn()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, print("נפתח דף כניסה למערכת"))
