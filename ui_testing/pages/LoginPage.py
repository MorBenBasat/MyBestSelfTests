import time

from locators.LoginPageLocators import LoginPageLocators
from pages.Pages_url import PagesUrlMbs
from test_users.login_users import SuccessLoginUser
from waits.wait import wait_for_element_presence, wait_for_element_clickable
from helpers.Helpers import HelpersMbs


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.pageUrl = PagesUrlMbs.login
        self.helpers = HelpersMbs(self.driver)

    def navigate_to_login_page(self):
        self.driver.maximize_window()
        self.helpers.navigation_to_url(self.pageUrl)

    def login(self, UserLogin):
        login_username_input_ = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_USERNAME)
        login_username_input_.send_keys(UserLogin.username)
        login_password_input = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_PASSWORD)
        login_password_input.send_keys(UserLogin.password)
        login_btn = wait_for_element_clickable(self.driver, *LoginPageLocators.LOGIN_BTN)
        HelpersMbs.delay(1)
        login_btn.click()
        HelpersMbs.delay(2)

    def success_login(self):
        self.driver.maximize_window()
        self.navigate_to_login_page()
        self.login(SuccessLoginUser)

    def fill_without_click_btn(self, UserLogin):
        login_username_input_ = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_USERNAME)
        login_username_input_.send_keys(UserLogin.username)
        login_password_input = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_PASSWORD)
        login_password_input.send_keys(UserLogin.password)
        time.sleep(1)

    def verify_login_page_mandatory_text(self, expected_text):
        selector = wait_for_element_presence(self.driver, *LoginPageLocators.USERNAME_FIELD_MANDATORY_TEXT)
        HelpersMbs.delay(1)

        if selector.text == expected_text:
            print('Text is as expected:', expected_text)
        else:
            print('Text is not as expected. Actual text:', selector.text)
        return selector.text

    def verify_login_page_length_alert(self, expected_text):
        selector = wait_for_element_presence(self.driver, *LoginPageLocators.LENGTH_ALERT)
        HelpersMbs.delay(1)

        if selector.text == expected_text:
            print('Text is as expected:', expected_text)
        else:
            print('Text is not as expected. Actual text:', selector.text)
        return selector.text

    def verify_title_login_name(self, expected_text):
        selector = wait_for_element_presence(self.driver, *LoginPageLocators.LOGO_LOGIN_NAME)
        HelpersMbs.delay(1)

        if selector.text == expected_text:
            print('text is as expected:', expected_text)
        else:
            print('', selector.text)
        return selector.text

    def success_login_alert(self, expected_text):
        alert = wait_for_element_presence(self.driver, *LoginPageLocators.SUCCESS_LOGIN_ALERT)
        HelpersMbs.delay(1)

        if alert.text == expected_text:
            print('text is as expected:', expected_text)
        else:
            print('Text is not as expected. Actual text:', alert.text)
        return alert.text

