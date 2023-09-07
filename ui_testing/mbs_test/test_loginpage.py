import time
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from locators.LoginPageLocators import LoginPageLocators
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from waits import wait
from waits.wait import wait_for_element_presence


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()  # Initialize the WebDriver
        self.helpers = HelpersMbs(self.driver)  # Create an instance of the LoginPage clas
        self.login_page = LoginPage(self.driver)  # Create an instance of the LoginPage class
        self.pageUrl = PagesUrlMbs.activities_details

    @pytest.mark.test29
    def test_successful_login(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        url = self.driver.current_url
        self.login_page.login("test", "258963")
        time.sleep(2)

        self.assertNotEqual(self.driver.current_url, url, "כניסה בוצעה בהצלחה")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test30
    def test_invalid_login(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        time.sleep(2)
        url = self.driver.current_url
        self.login_page.login("invalid", "invalid")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test31
    def test_valid_username_invalid_password(self):
        self.login_page.navigate_to_login_page()
        url = self.driver.current_url
        self.login_page.login("test", "1111111")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test32
    def test_invalid_username_valid_password(self):
        self.login_page.navigate_to_login_page()
        url = self.driver.current_url
        self.login_page.login("invalidInput", "258963")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test33
    def test_only_password(self):
        self.login_page.navigate_to_login_page()
        time.sleep(2)
        url = self.driver.current_url
        self.login_page.login("", "258963")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test34
    def test_only_username(self):
        self.login_page.navigate_to_login_page()
        url = self.driver.current_url
        self.login_page.login("test", "")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()


