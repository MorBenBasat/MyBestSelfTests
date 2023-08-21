from ui_testing.pages.LoginPage import LoginPage
from ui_testing.waits.wait import wait_for_element_presence, wait_for_element_visibility, wait_for_element_clickable
import time
from ui_testing.pages.pages_url import MbsUrl


class ViewData:

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.page_url = MbsUrl(driver)

    def login_the_system(self, username, password):
        self.login_page.navigate_to_login_page()
        self.login_page.login_username(username)
        self.login_page.login_password(password)
        self.login_page.login_button()
        time.sleep(5)

    def open_view_data_page(self):
        view_data = self.page_url.my_profile_page_url()
        if self.driver.current_url != view_data:
            print("My profile page is open")
        else:
            print("My profile page is not open")