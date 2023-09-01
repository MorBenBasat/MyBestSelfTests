import time
import unittest

import pytest
from selenium import webdriver
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()  # Initialize the WebDriver
        self.helpers = HelpersMbs(self.driver)  # Create an instance of the LoginPage clas
        self.login_page = LoginPage(self.driver)  # Create an instance of the LoginPage class

    @pytest.mark.smoke
    def test_successful_login(self):
        self.login_page.navigate_to_login_page()
        url = self.driver.current_url
        self.login_page.login("test", "258963")
        time.sleep(4)

        self.assertNotEqual(self.driver.current_url, url, "כניסה בוצעה בהצלחה")
        self.helpers.alerts_login()

    @pytest.mark.invalid
    def test_invalid_login(self):
        self.login_page.navigate_to_login_page()
        time.sleep(2)
        url = self.driver.current_url
        self.login_page.login("invalid", "invalid")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()

    def test_valid_username_invalid_password(self):
        self.login_page.navigate_to_login_page()
        url = self.driver.current_url
        self.login_page.login("test", "1111111")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()

    def test_invalid_username_valid_password(self):
        self.login_page.navigate_to_login_page()
        url = self.driver.current_url
        self.login_page.login("invalidInput", "258963")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()

    def test_only_password(self):
        self.login_page.navigate_to_login_page()
        time.sleep(2)
        url = self.driver.current_url
        self.login_page.login("", "258963")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()

    def test_only_username(self):
        self.login_page.navigate_to_login_page()
        url = self.driver.current_url
        self.login_page.login("test", "")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()

    def test_no_inputs(self):
        self.login_page.navigate_to_login_page()
        url = self.driver.current_url
        self.login_page.login("test", "")
        self.assertEqual(self.driver.current_url, url, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
