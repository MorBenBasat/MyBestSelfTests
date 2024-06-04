import unittest

from helpers.DisconnectSystem import DisconnectSystem
from initialize_driver import initialize_driver
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs


class TestActivitiesDetailsPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.disconnect_system = DisconnectSystem(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_click_disconnect_btn(self):
        self.login_page.success_login()
        self.disconnect_system.click_on_disconnect_btn()
        self.assertEqual(PagesUrlMbs.logout, self.driver.current_url,
                         print("login page open after click on disconnect btn"))

    def test_click_on_logo(self):
        self.login_page.success_login()
        self.disconnect_system.click_on_logo()
        self.assertEqual(PagesUrlMbs.login, self.driver.current_url,
                         print("login page open after click on logo"))

    def test_verify_fields_cleared(self):
        self.login_page.success_login()
        self.disconnect_system.click_on_disconnect_btn()
        self.disconnect_system.verify_username_is_clear()

    def tearDown(self):
        self.driver.quit()


