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

