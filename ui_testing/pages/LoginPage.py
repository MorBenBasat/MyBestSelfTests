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
        login_username_input_.send_keys(UserLogin.login)  # שם משתמש : טסס
        login_password_input = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_PASSWORD)
        login_password_input.send_keys(UserLogin.password)  # סיסמא : 258963
        login_btn = wait_for_element_clickable(self.driver, *LoginPageLocators.LOGINPAGE_BTN)
        HelpersMbs.delay(1)
        login_btn.click()
        HelpersMbs.delay(2)

    def success_login(self):
        self.driver.maximize_window()
        self.navigate_to_login_page()
        self.login(SuccessLoginUser)
        HelpersMbs.delay(2)

    def verify_username_and_mandatory_text(self, expected_text):
        username_mandatory_field_text = wait_for_element_presence(self.driver,
                                                                  *LoginPageLocators.USERNAME_FIELD_MANDATORY_ALERT)

        # Check if the text of the element matches the expected text
        if username_mandatory_field_text.text == expected_text:
            print('Text is as expected:', expected_text)
        else:
            print('Text is not as expected. Actual text:', username_mandatory_field_text.text)

    def verify_password_and_mandatory_text(self, expected_text):
        password_mandatory_field_text = wait_for_element_presence(self.driver,
                                                                  *LoginPageLocators.PASSWORD_FIELD_MANDATORY_ALERT)

        # Check if the text of the element matches the expected text
        if password_mandatory_field_text.text == expected_text:
            print('Text is as expected:', expected_text)
        else:
            print('Text is not as expected. Actual text:', password_mandatory_field_text.text)

    def is_login_button_enabled(self, LoginErrorLength):
        username_input = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_USERNAME)
        password_input = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_PASSWORD)

        username_input.send_keys(LoginErrorLength.login)
        password_input.send_keys(LoginErrorLength.password)

        login_btn = wait_for_element_clickable(self.driver, *LoginPageLocators.LOGINPAGE_BTN)

        username_length = len(username_input.get_attribute('value'))
        password_length = len(password_input.get_attribute('value'))

        is_username_valid = 6 <= username_length <= 12
        is_password_valid = 6 <= password_length <= 12

        return is_username_valid and is_password_valid and login_btn.is_enabled()
