import unittest
import pytest

from locators.SignUpLocators import SignUpLocators
from pages.Pages_url import PagesUrlMbs
from pages.SignUpPage import SignUpPage
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from test_users.register_users import ValidRegistrationUser, NoPasswordRegistration, \
    DifferentPasswordAndConfirm, NoFirstNameRegistration, NoLastNameRegistration, NoFillRegistrationFields \
    , InvalidLengthUserName, InvalidLengthPassword


class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.signup_page = SignUpPage(self.driver)

    @pytest.mark.test36
    def test_success_navigation_sign_up_page(self):
        self.signup_page.navigate_to_signup_page()
        HelpersMbs.delay(2)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.register, print("Sign Up Page Open"))
        self.driver.quit()

    @pytest.mark.test37
    def test_success_registration(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_and_login(ValidRegistrationUser)
        alert = self.helpers.alerts_signup()

        HelpersMbs.delay(2)
        self.assertEqual(
            alert,
            f'כניסה למערכת\nברוך הבא {ValidRegistrationUser.username}')
        print(alert)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.my_profile, "כניסה בוצעה בהצלחה")
        self.driver.quit()

    @pytest.mark.test38
    def test_create_user_without_password(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_register(NoPasswordRegistration)
        self.assertEqual(register_btn_disable, True, print("כפתור מוצג לא לחיץ"))
        self.driver.quit()

    @pytest.mark.test39
    def test_no_fll_signup_fields(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_register(NoFillRegistrationFields)
        self.assertEqual(register_btn_disable, True, print("כפתור מוצג לא לחיץ"))
        self.driver.quit()

    @pytest.mark.test40
    def test_different_confirm_and_password(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_register(DifferentPasswordAndConfirm)
        self.assertEqual(register_btn_disable, True, print("כפתור מוצג לא לחיץ"))
        self.driver.quit()

    @pytest.mark.test46
    def test_fill_without_first_name_field(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_register(NoFirstNameRegistration)
        self.assertEqual(register_btn_disable, True, print("כפתור מוצג לא לחיץ"))
        self.driver.quit()

    @pytest.mark.test47
    def test_fill_without_last_name_field(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_register(NoLastNameRegistration)
        self.assertEqual(register_btn_disable, True, print("כפתור מוצג לא לחיץ"))

        self.driver.quit()

    @pytest.mark.test48
    def test_invalid_email_input(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_user_without_click_btn(NoLastNameRegistration)

        self.assertEqual(register_btn_disable, True, print("כפתור מוצג לא לחיץ"))
        self.driver.quit()

    @pytest.mark.test54
    def test_invalid_username_length(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_register(InvalidLengthUserName)
        self.assertEqual(register_btn_disable, True, print("כפתור מוצג לא לחיץ"))
        self.driver.quit()

    @pytest.mark.test95
    def test_invalid_password_length(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_register(InvalidLengthPassword)
        self.assertEqual(register_btn_disable, True, print("כפתור מוצג לא לחיץ"))
        self.driver.quit()

    @pytest.mark.test96
    def test_verify_gender_pick(self):
        self.signup_page.navigate_to_signup_page()
        is_clicked = self.signup_page.gender_verify_click_radio_button()
        self.assertTrue(is_clicked, f"The gender selection should be successful. Selected gender: {is_clicked}")
        HelpersMbs.delay(2)

    @pytest.mark.test97
    def test_create_with_same_username(self):
        self.signup_page.navigate_to_signup_page()
        result_message = self.signup_page.create_with_same_field(ValidRegistrationUser)
        expected_message = "user already exists"
        self.assertEqual(result_message, expected_message, "Expected message does not match actual message.")
        HelpersMbs.delay(2)

    @pytest.mark.test116
    def test_create_user_with_all_fields(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(ValidRegistrationUser)
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.assertEqual(register_btn_disable, False, print("כפתור מוצג לחיץ"))
        self.driver.quit()
