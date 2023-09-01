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
        self.loginpage = LoginPage(self.driver)
        self.signup_page = SignUpPage(self.driver)

    def test_success_navigation_sign_up_page(self):
        self.loginpage.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        time.sleep(2)
        url = self.driver.current_url
        self.assertEqual('http://localhost:4200/register', url, "Sign Up Page Open")
