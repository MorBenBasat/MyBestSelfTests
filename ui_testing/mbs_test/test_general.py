import unittest

from helpers.AlertsAndStrings import LogoOpenMyProfile
from helpers.Helpers import HelpersMbs
from initialize_driver import initialize_driver
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs


class TestActivitiesDetailsPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_click_on_logo(self):
        self.login_page.navigate_to_login_page()
        self.login_page.success_login()
        self.helpers.click_on_logo()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.my_profile, print(LogoOpenMyProfile.my_string))

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
