import unittest
import pytest
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from locators.LoginPageLocators import LoginPageLocators
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.login_users import ValidNameInvalidPassword, InvalidLogin, InValidNameValidPassword, \
    NoFillUserName, NoFillPassword, SuccessLoginUser, InvalidUsernameLength


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)

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
        self.driver.quit()

    @pytest.mark.test34
    def test_only_username(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login(NoFillPassword)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, "שם משתמש או הסיסמא לא נכונים ")
        self.driver.quit()

    def test_verify_username_mandatory_text(self):
        self.login_page.navigate_to_login_page()
        expected_text = 'נא מלא שדה זה לפני שליחה'
        self.login_page.verify_username_and_mandatory_text(expected_text)

    def test_verify_password_mandatory_text(self):
        self.login_page.navigate_to_login_page()
        expected_text = 'נא מלא שדה זה לפני שליחה'
        self.login_page.verify_password_and_mandatory_text(expected_text)

    def test_btn_is_field_invalid_and_dirty(self):
        self.login_page.navigate_to_login_page()
        is_username_field_valid = HelpersMbs.is_field_valid(self.driver, LoginPageLocators.LOGINPAGE_USERNAME)
        is_password_field_valid = HelpersMbs.is_field_valid(self.driver, LoginPageLocators.LOGINPAGE_PASSWORD)

        if not is_username_field_valid or not is_password_field_valid:
            login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGINPAGE_BTN)
            self.assertEqual(login_btn_disable, True, 'כפתור מוצג לא לחיץ')

    def test_btn_is_field_valid(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login_without_click_btn(SuccessLoginUser)
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGINPAGE_BTN)
        if login_btn_disable:
            self.assertEqual(login_btn_disable, True, 'כפתור מוצג לחיץ')

    def test_invalid_username_length(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login_without_click_btn(InvalidUsernameLength)
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGINPAGE_BTN)
        if login_btn_disable:
            self.assertEqual(login_btn_disable, True, 'כפתור מוצג לא לחיץ')

    def test_invalid_password_length(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login_without_click_btn(InvalidUsernameLength)
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGINPAGE_BTN)
        if login_btn_disable:
            self.assertEqual(login_btn_disable, True, 'כפתור מוצג לא לחיץ')
