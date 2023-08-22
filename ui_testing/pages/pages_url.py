import time

from pages.LoginPage import LoginPage


class MbsUrl:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def main_url(self):
        self.login_page.navigate_to_login_page()

    def register_page_url(self):
        self.driver.get("http://localhost:4200/register")

    def view_data_url(self):
        self.driver.get("http://localhost:4200/my-profile")

    def agenda_page(self):
        self.driver.get("http://localhost:4200/agenda")
