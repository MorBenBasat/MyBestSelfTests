import unittest

from helpers.Helpers import HelpersMbs
from initialize_driver import initialize_driver
from pages.LoginPage import LoginPage


class TestActivitiesPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
