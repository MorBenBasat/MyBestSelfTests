from helpers import Helpers
from helpers.Helpers import HelpersMbs
from locators.DisconnectSystemLocators import DisconnectSystemLocators
from locators.LoginPageLocators import LoginPageLocators
from pages.Pages_url import PagesUrlMbs
from test_users.login_users import SuccessLoginUser
from waits.wait import wait_for_element_presence, wait_for_element_clickable
from pages.LoginPage import LoginPage


class DisconnectSystem:

    def __init__(self, driver):
        self.driver = driver
        self.pageUrl = PagesUrlMbs.login
        self.login_page = LoginPage(self.driver)

    def click_on_disconnect_btn(self):
        click_on_btn = wait_for_element_clickable(self.driver, *DisconnectSystemLocators.DISCONNECT_BTN)
        click_on_btn.click()

    def click_on_logo(self):
        click_on_logo = wait_for_element_clickable(self.driver, *DisconnectSystemLocators.LOGO)
        click_on_logo.click()

    def verify_username_is_clear(self):
        username_input = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_USERNAME)
        HelpersMbs.delay(1)
        username_value = username_input.get_attribute("value")
        if username_value == "":
            print("Username field is clear")
            return username_value
        else:
            raise Exception("Username field is not clear")
