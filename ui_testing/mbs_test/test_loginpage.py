import unittest
import pytest

from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from locators.LoginPageLocators import LoginPageLocators
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.login_users import ValidNameInvalidPassword, InvalidLogin, InValidNameValidPassword, \
    NoFillUserName, NoFillPassword, SuccessLoginUser, InvalidUsernameLength, InvalidPasswordLength


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)

    @pytest.mark.test29
    def test_successful_login(self):
        self.login_page.success_login()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.my_profile, "כניסה בוצעה בהצלחה")
        print(self.helpers.alerts_login())
        self.driver.quit()

    @pytest.mark.test30
    def test_invalid_login(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.DISABLE_LOGINPAGE_BTN)
        self.login_page.fill_without_click_btn(InvalidLogin)
        self.assertEqual(login_btn_disable, True, 'כפתור מוצג לא לחיץ')
        HelpersMbs.delay(2)
        self.driver.quit()

    @pytest.mark.test31
    def test_valid_username_invalid_password(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.DISABLE_LOGINPAGE_BTN)
        self.login_page.fill_without_click_btn(ValidNameInvalidPassword)
        self.assertEqual(login_btn_disable, True, 'כפתור מוצג לא לחיץ')
        self.driver.quit()

    @pytest.mark.test32
    def test_invalid_username_valid_password(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.DISABLE_LOGINPAGE_BTN)
        self.login_page.fill_without_click_btn(InValidNameValidPassword)
        self.assertEqual(login_btn_disable, True, 'כפתור מוצג לא לחיץ')
        self.driver.quit()

    @pytest.mark.test33
    def test_only_password(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.DISABLE_LOGINPAGE_BTN)
        self.login_page.fill_without_click_btn(NoFillUserName)
        self.assertEqual(login_btn_disable, True, 'כפתור מוצג לא לחיץ')
        self.driver.quit()

    @pytest.mark.test34
    def test_only_username(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.DISABLE_LOGINPAGE_BTN)
        self.login_page.login(NoFillPassword)
        self.assertEqual(login_btn_disable, True, print('כפתור מוצג לא לחיץ'))
        self.driver.quit()

    @pytest.mark.test98
    def test_verify_mandatory_login_page_text(self):
        self.login_page.navigate_to_login_page()
        expected_text = 'נא מלא שדה זה לפני שליחה'
        actual_text = self.login_page.verify_login_page_mandatory_text(expected_text)
        self.assertEqual(actual_text, expected_text, print('טקסט דרישת מילוי מופיע'))

    def test_btn_is_field_invalid_and_dirty(self):
        self.login_page.navigate_to_login_page()
        is_username_field_valid = HelpersMbs.is_field_valid(self.driver, LoginPageLocators.LOGINPAGE_USERNAME)
        is_password_field_valid = HelpersMbs.is_field_valid(self.driver, LoginPageLocators.LOGINPAGE_PASSWORD)

        if not is_username_field_valid or not is_password_field_valid:
            login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.DISABLE_LOGINPAGE_BTN)
            self.assertEqual(login_btn_disable, True, 'כפתור מוצג לא לחיץ')

    def test_btn_is_field_valid(self):
        self.login_page.navigate_to_login_page()
        login_btn_enabled = HelpersMbs.is_enabled(self.driver, LoginPageLocators.DISABLE_LOGINPAGE_BTN)
        self.login_page.fill_without_click_btn(SuccessLoginUser)
        HelpersMbs.delay(2)
        self.assertEqual(login_btn_enabled, True, print('כפתור מוצג לחיץ'))

        self.driver.quit()

    def test_invalid_username_length(self):
        self.login_page.navigate_to_login_page()
        login_btn_enabled = HelpersMbs.is_enabled(self.driver, LoginPageLocators.DISABLE_LOGINPAGE_BTN)
        self.login_page.fill_without_click_btn(InvalidUsernameLength)
        HelpersMbs.delay(2)
        self.assertEqual(login_btn_enabled, False, print('כפתור מוצג לא לחיץ'))

        self.driver.quit()

    def test_invalid_password_length(self):
        self.login_page.navigate_to_login_page()
        login_btn_enabled = HelpersMbs.is_enabled(self.driver, LoginPageLocators.DISABLE_LOGINPAGE_BTN)
        self.login_page.fill_without_click_btn(InvalidPasswordLength)
        HelpersMbs.delay(2)
        self.assertEqual(login_btn_enabled, False, print('כפתור מוצג לא לחיץ'))

        self.driver.quit()

    def test_invalid_length_username_password(self):
        self.login_page.navigate_to_login_page()
        login_btn_enabled = HelpersMbs.is_enabled(self.driver, LoginPageLocators.DISABLE_LOGINPAGE_BTN)
        self.login_page.fill_without_click_btn(InvalidPasswordLength)
        HelpersMbs.delay(2)
        self.assertEqual(login_btn_enabled, False, print('כפתור מוצג לא לחיץ'))

        self.driver.quit()
