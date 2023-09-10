import unittest
import pytest
from pages.Agenda.ActivitiesPage import ActivitiesPage
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.Agenda.ActivitiesDetailsPage import ActivitiesDetailsPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs


class TestActivitiesPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.activities_details_page = ActivitiesDetailsPage(self.driver)
        self.activities_page = ActivitiesPage(self.driver)
        self.agenda_page = MyAgendaPage(self.driver)

    def test_success_navigation_activities_page(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login('test', '258963')
        url = self.driver.current_url
        self.activities_page.navigate_to_activities_page()
        self.assertNotEqual(PagesUrlMbs.activities, url, print('Activities page opens propelry'))

    def test_open_activities_by_drop_list(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login('test','258963')
        HelpersMbs.delay(2)
        url = self.driver.current_url
        self.activities_page.navigate_to_activities_page_by_drop_list()
        self.assertNotEqual(PagesUrlMbs.activities, url, print('Activities Details Page Open By Drop List'))
