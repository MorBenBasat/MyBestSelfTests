import unittest
import pytest
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.login_users import ValidNameInvalidPassword, InvalidLogin, InValidNameValidPassword, \
    NoFillUserName, NoFillPassword


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_driver()  # Initialize the WebDriver
        self.helpers = HelpersMbs(self.driver)  # Create an instance of the LoginPage class
        self.login_page = LoginPage(self.driver)  # Create an instance of the LoginPage class

    @pytest.mark.test29
    def test_successful_login(self):
        self.login_page.success_login()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.my_profile, "כניסה בוצעה בהצלחה")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test30
    def test_invalid_login(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        HelpersMbs.delay(2)

        self.login_page.login(InvalidLogin)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, print("שם משתמש או הסיסמא לא נכונים "))
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test31
    def test_valid_username_invalid_password(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(ValidNameInvalidPassword)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login,print( "שם משתמש או הסיסמא לא נכונים "))
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test32
    def test_invalid_username_valid_password(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(InValidNameValidPassword)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test33
    def test_only_password(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        HelpersMbs.delay(2)
        self.login_page.login(NoFillUserName)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test34
    def test_only_username(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(NoFillPassword)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, "שם משתמש או הסיסמא לא נכונים ")
        self.helpers.alerts_login()
        self.driver.quit()
