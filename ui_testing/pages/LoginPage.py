import time
from locators.LoginPageLocators import LoginPageLocators
from waits.wait import wait_for_element_presence, wait_for_element_visibility, wait_for_element_clickable


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self, page):
        base_url = "http://localhost:4200/login"
        self.driver.get(base_url)
        time.sleep(3)

    def login(self, username, password):
        login_username_input_ = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_USERNAME)
        login_username_input_.send_keys(username)  # שם משתמש : טסס
        login_password_input = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_PASSWORD)
        login_password_input.send_keys(password)  # סיסמא : 258963
        login_btn = wait_for_element_clickable(self.driver, *LoginPageLocators.LOGINPAGE_BTN)
        time.sleep(1)
        login_btn.click()


# -----------------------------------------------------------------------------------------------------