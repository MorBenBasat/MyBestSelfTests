import unittest
import pytest

from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from locators.LoginPageLocators import LoginPageLocators
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.login_users import ValidNameInvalidPassword, InvalidLogin, InValidNameValidPassword, \
    NoFillUserName, NoFillPassword, SuccessLoginUser, UserNameInvalidLength, PasswordInvalidLength, \
    FillInvalidLengthFields, UserTestForLengthAlert


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)

    @pytest.mark.test29
    def test_successful_login(self):
        self.login_page.success_login()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.my_profile,print("כניסה בוצעה בהצלחה"))
        self.driver.quit()

    @pytest.mark.test30
    def test_invalid_login(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGIN_BTN)
        self.login_page.fill_without_click_btn(InvalidLogin)
        self.assertEqual(login_btn_disable, True, print('כפתור מוצג לחיץ'))
        HelpersMbs.delay(2)
        self.driver.quit()

    @pytest.mark.test31
    def test_valid_username_invalid_password(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGIN_BTN)
        self.login_page.fill_without_click_btn(ValidNameInvalidPassword)
        self.assertEqual(login_btn_disable, True,print('כפתור מוצג לא לחיץ'))
        self.driver.quit()

    @pytest.mark.test32
    def test_invalid_username_valid_password(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGIN_BTN)
        self.login_page.fill_without_click_btn(InValidNameValidPassword)
        HelpersMbs.delay(1)
        self.assertEqual(login_btn_disable, True, print('כפתור מוצג לא לחיץ'))
        self.driver.quit()

    @pytest.mark.test33
    def test_only_password(self):
        self.login_page.navigate_to_login_page()
        self.login_page.fill_without_click_btn(NoFillUserName)
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGIN_BTN)
        self.assertEqual(login_btn_disable, True, print('כפתור מוצג לא לחיץ'))
        self.driver.quit()

    @pytest.mark.test34
    def test_only_username(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGIN_BTN)
        self.login_page.fill_without_click_btn(NoFillPassword)
        HelpersMbs.delay(1)
        self.assertEqual(login_btn_disable, True, print('כפתור מוצג לא לחיץ'))
        self.driver.quit()

    @pytest.mark.test98
    def test_verify_mandatory_login_page_text(self):
        self.login_page.navigate_to_login_page()
        expected_text = 'נא מלא שדה זה לפני שליחה'
        actual_text = self.login_page.verify_login_page_mandatory_text(expected_text)
        self.assertEqual(actual_text, expected_text)

    def test_btn_is_field_invalid_and_dirty(self):
        self.login_page.navigate_to_login_page()
        is_username_field_valid = HelpersMbs.is_field_valid(self.driver, LoginPageLocators.LOGINPAGE_USERNAME)
        is_password_field_valid = HelpersMbs.is_field_valid(self.driver, LoginPageLocators.LOGINPAGE_PASSWORD)

        if not is_username_field_valid or not is_password_field_valid:
            login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGIN_BTN)
            self.assertEqual(login_btn_disable, True, 'כפתור מוצג לא לחיץ')

    @pytest.mark.test119
    def test_btn_is_field_valid(self):
        self.login_page.navigate_to_login_page()
        self.login_page.fill_without_click_btn(SuccessLoginUser)
        login_btn_enabled = not HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGIN_BTN)
        self.assertEqual(login_btn_enabled, True, print('כפתור מוצג לחיץ'))

        self.driver.quit()

    def test_invalid_username_length(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGIN_BTN)
        self.login_page.fill_without_click_btn(UserNameInvalidLength)
        HelpersMbs.delay(2)
        self.assertEqual(login_btn_disable, True, print('כפתור מוצג לא לחיץ'))

        self.driver.quit()

    def test_invalid_password_length(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGIN_BTN)
        self.login_page.fill_without_click_btn(PasswordInvalidLength)
        HelpersMbs.delay(1)
        self.assertEqual(login_btn_disable, True, print('כפתור מוצג לא לחיץ'))

        self.driver.quit()

    def test_invalid_length_username_password(self):
        self.login_page.navigate_to_login_page()
        login_btn_disable = HelpersMbs.is_disabled(self.driver, LoginPageLocators.LOGIN_BTN)
        self.login_page.fill_without_click_btn(FillInvalidLengthFields)
        HelpersMbs.delay(1)
        self.assertEqual(login_btn_disable, True, print('כפתור מוצג לא לחיץ'))

        self.driver.quit()

    def test_is_display_invalid_length_alert(self):
        self.login_page.navigate_to_login_page()
        expected_text = 'המינימום תווים בשדה זה הוא 6'
        self.login_page.fill_without_click_btn(UserTestForLengthAlert)
        actual_text = self.login_page.verify_login_page_length_alert(expected_text)
        self.assertEqual(expected_text, actual_text, 'טקסט דרישת מילוי מופיע')

    def test_title_login_name(self):
        self.login_page.navigate_to_login_page()
        expected_text = 'כניסה למערכת'
        actual_text = self.login_page.verify_title_login_name(expected_text)
        self.assertEqual(actual_text, expected_text, 'כותרת מציגה כניסה למערכת')

    def test_verify_success_alert_text(self):
        self.login_page.success_login()
        expected_text = f'כניסה למערכת\nברוך הבא {SuccessLoginUser.username}'
        actual_text = self.login_page.success_login_alert(expected_text)

        self.assertEqual(actual_text, expected_text)
