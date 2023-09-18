import unittest
import pytest
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.login_users import ValidNameInvalidPassword, InvalidLogin, InValidNameValidPassword, \
    NoFillUserName, NoFillPassword, PasswordInvalidLength, UserNameInvalidLength, NoFillDetails


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver()  # Initialize the WebDriver
        self.helpers = HelpersMbs(self.driver)  # Create an instance of the LoginPage class
        self.login_page = LoginPage(self.driver)  # Create an instance of the LoginPage class

    @pytest.mark.test29
    def test_successful_login(self):
        self.login_page.success_login()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.my_profile, "כניסה בוצעה בהצלחה")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test30
    def test_invalid_login(self):
        self.login_page.navigate_to_login_page()
        HelpersMbs.delay(2)

        self.login_page.login(InvalidLogin)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, print("שם משתמש או הסיסמא לא נכונים "))
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test31
    def test_valid_username_invalid_password(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login(ValidNameInvalidPassword)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, print("שם משתמש או הסיסמא לא נכונים "))
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test32
    def test_invalid_username_valid_password(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login(InValidNameValidPassword)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test33
    def test_only_password(self):
        self.login_page.navigate_to_login_page()
        HelpersMbs.delay(2)
        self.login_page.login(NoFillUserName)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test34
    def test_only_username(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login(NoFillPassword)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()

    def test_verify_username_mandatory_text(self):
        self.login_page.navigate_to_login_page()
        expected_text = 'נא למלא שדה שם משתמש'
        self.login_page.verify_username_and_mandatory_text(expected_text)

    def test_verify_password_mandatory_text(self,expected_text):
        self.login_page.navigate_to_login_page()
        expected_text = 'נא למלא שדה סיסמא'
        self.login_page.verify_password_and_mandatory_text(expected_text)

    def test_login_button_state_invalid_length(self):
        self.login_page.navigate_to_login_page()

        assert not self.login_page.is_login_button_enabled(NoFillDetails), "כפתור לוגין לא מופיע לחיתץ"

        assert not self.login_page.is_login_button_enabled(PasswordInvalidLength)

        self.login_page.login(ValidNameInvalidPassword)

        # Now, the login button should be enabled
        assert self.login_page.is_login_button_enabled(ValidNameInvalidPassword), "כפתור כניסה מופיע לחי"
