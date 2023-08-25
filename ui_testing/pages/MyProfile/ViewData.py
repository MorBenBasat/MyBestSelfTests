from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from waits.wait import wait_for_element_presence, wait_for_element_visibility, wait_for_element_clickable
import time
from pages.pages_url import PagesUrl, PagesUrlMbs


class ViewData:

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.base_url = HelpersMbs(driver)

    def login_the_system(self, username, password):
        self.login_page.navigate_to_login_page()
        self.login_page.login_username(username)
        self.login_page.login_password(password)
        self.login_page.login_button()
        time.sleep(5)

    def open_view_data_page(self):
        self.base_url.navigation_to_base_url(PagesUrlMbs.login)

        if self.driver.current_url != self.base_url:
            print("My profile page is open")
        else:
            print("My profile page is not open")


