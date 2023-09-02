import time
import unittest
from pages.SignUpPage import SignUpPage
import pytest
from selenium import webdriver
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage


class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.signup_page = SignUpPage(self.driver)

    def test_success_navigation_sign_up_page(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        time.sleep(2)
        url = self.driver.current_url
        self.assertEqual('http://localhost:4200/register', url, "Sign Up Page Open")
        self.driver.quit()

    def test_create_user_without_password(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register('test', 'test', 'test@gmail.com', 'test', 'נקבה', '', '21111')
        