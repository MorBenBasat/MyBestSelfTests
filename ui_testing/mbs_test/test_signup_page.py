import unittest
import pytest

from helpers.AlertsAndStrings import CompareTextFail, DisableBtn, AfterRegisterLoginSystem, AbleBtn, UserCreate, \
    UserExist, SuccessLogin, SignUpPageOpen, UserCreateText
from locators.SignUpLocators import SignUpLocators
from pages.Pages_url import PagesUrlMbs
from pages.SignUpPage import SignUpPage
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from test_users.register_users import ValidRegistrationUser, NoPasswordRegistration, \
    DifferentPasswordAndConfirm, NoFirstNameRegistration, NoLastNameRegistration, NoFillRegistrationFields \
    , InvalidLengthUserName, InvalidLengthPassword, ValidRegisterUserExist


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
        self.assertEqual(self.driver.current_url, PagesUrlMbs.register, print(SignUpPageOpen.my_string))
        self.driver.quit()

    def test_create_registration(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(ValidRegistrationUser)
        alert = self.helpers.alerts_display()
        expected_alert_message = UserCreateText.alert

        HelpersMbs.delay(1)
        self.assertEqual(alert, expected_alert_message, print(UserCreate.my_string))

    @pytest.mark.test37
    def test_success_registration_and_login(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_and_login(ValidRegistrationUser)
        alert = self.helpers.alerts_display()

        HelpersMbs.delay(1)
        self.assertEqual(
            alert,
            AfterRegisterLoginSystem.alert)
        print(alert)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.my_profile,SuccessLogin.my_string)
        self.driver.quit()

    @pytest.mark.test38
    def test_create_user_without_password(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_user_without_click_btn(NoPasswordRegistration)
        self.assertEqual(register_btn_disable, True, print(DisableBtn.my_string))
        self.driver.quit()

    @pytest.mark.test39
    def test_no_fll_signup_fields(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_user_without_click_btn(NoFillRegistrationFields)
        self.assertEqual(register_btn_disable, True, print(DisableBtn.my_string))
        self.driver.quit()

    @pytest.mark.test40
    def test_different_confirm_and_password(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_user_without_click_btn(DifferentPasswordAndConfirm)
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.assertEqual(register_btn_disable, False, print(DisableBtn.my_string))
        self.driver.quit()

    @pytest.mark.test46
    def test_fill_without_first_name_field(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_user_without_click_btn(NoFirstNameRegistration)
        self.assertEqual(register_btn_disable, True, print(DisableBtn.my_string))
        self.driver.quit()

    @pytest.mark.test47
    def test_fill_without_last_name_field(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_user_without_click_btn(NoLastNameRegistration)
        self.assertEqual(register_btn_disable, True, print(DisableBtn.my_string))

        self.driver.quit()

    @pytest.mark.test48
    def test_invalid_email_input(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_user_without_click_btn(NoLastNameRegistration)
        self.assertEqual(register_btn_disable, True, print(DisableBtn.my_string))

        self.driver.quit()

    @pytest.mark.test54
    def test_invalid_username_length(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_user_without_click_btn(InvalidLengthUserName)
        self.assertEqual(register_btn_disable, True, print(DisableBtn.my_string))
        self.driver.quit()

    @pytest.mark.test95
    def test_invalid_password_length(self):
        self.signup_page.navigate_to_signup_page()
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.signup_page.create_user_without_click_btn(InvalidLengthPassword)
        self.assertEqual(register_btn_disable, True, print(DisableBtn.my_string))
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
        result_message = self.signup_page.create_with_same_field(ValidRegisterUserExist)
        expected_message = UserExist.alert
        self.assertEqual(result_message, expected_message, CompareTextFail.my_string)
        HelpersMbs.delay(2)

    @pytest.mark.test116
    def test_create_user_with_all_fields(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_user_without_click_btn(ValidRegistrationUser)
        register_btn_disable = HelpersMbs.is_disabled(self.driver, SignUpLocators.REGISTER_CREATE_BTN)
        self.assertEqual(register_btn_disable, False, print(AbleBtn.my_string))
        self.driver.quit()
