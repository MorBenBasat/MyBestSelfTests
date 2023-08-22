import time
from locators.LoginPageLocators import LoginPageLocators
from waits.wait import wait_for_element_presence, wait_for_element_visibility, wait_for_element_clickable


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self):
        base_url = "http://localhost:4200/login"
        self.driver.get(base_url)
        time.sleep(3)

    def login_username(self, username):
        login_username_input_ = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_USERNAME)
        login_username_input_.send_keys(username)  # שם משתמש : טסס

    def login_password(self, password):
        login_password_input = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_PASSWORD)
        login_password_input.send_keys(password)  # סיסמא : 258963

    def login_button(self):
        login_btn = wait_for_element_clickable(self.driver, *LoginPageLocators.LOGINPAGE_BTN)
        time.sleep(1)
        login_btn.click()
        LoginPage.alerts(self)

    def alerts(self):
        green_msg = wait_for_element_visibility(self.driver, *LoginPageLocators.GREEN_MSG)
        error_msg = wait_for_element_visibility(self.driver, *LoginPageLocators.ERROR_MSG)
        if green_msg.is_displayed():
            verify_green_msg = green_msg.text
            print('green msg display', verify_green_msg)

        elif error_msg.is_displayed():
            verify_error_msg = error_msg.text
            print('error connect system', verify_error_msg)


# -----------------------------------------------------------------------------------------------------
# Negative tests for login

class NegativeLogin:

    def __init__(self, driver):
        self.driver = driver
        self.login_system = LoginPage(self.driver)

    def invalid_username_valid_password(self, invalid_username, valid_password):
        invalid_user_input = wait_for_element_visibility(self.driver, *LoginPageLocators.LOGINPAGE_USERNAME)
        invalid_user_input.send_keys(invalid_username)

        valid_password_input = wait_for_element_visibility(self.driver, *LoginPageLocators.LOGINPAGE_PASSWORD)
        valid_password_input.send_keys(valid_password)

        button_click = wait_for_element_clickable(self.driver, *LoginPageLocators.LOGINPAGE_BTN)
        button_click.click()
        self.login_system.alerts()

    def valid_username_invalid_password (self):
        pass
