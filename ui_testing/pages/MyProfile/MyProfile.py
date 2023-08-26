from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from waits.wait import wait_for_element_presence, wait_for_element_visibility, wait_for_element_clickable
import time
from pages.pages_url import PagesUrl, PagesUrlMbs


class MyProfile:

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.base_url = HelpersMbs(driver)


