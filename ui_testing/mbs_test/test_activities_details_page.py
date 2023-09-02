import time
import unittest
import pytest

from pages.Agenda.ActivitiesPage import ActivitiesPage

from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.Agenda.ActivitiesDetailsPage import ActivitiesDetailsPage
from pages.LoginPage import LoginPage


class TestActivitiesDetailsPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.activities_details_page = ActivitiesDetailsPage(self.driver)
        self.activities_page = ActivitiesPage(self.driver)

    @pytest.mark.smoke
    def test_success_navigation_activities_page(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login('test', '258963')
        self.activities_details_page.navigate_to_activities_details_page()
        url = self.driver.current_url
        self.assertEqual("http://localhost:4200/activities-details/0", url, 'Activities Details Page Open!')
        self.driver.quit()


    def test_create_mission(self):
        self.helpers.navigation_to_url(self.login_page)
        self.login_page.login('test', '258963')

        self.helpers.navigation_to_url(self.activities_details_page)
        self.activities_details_page.fill_all_activities_details('sanitytest', 'sanity test')
        time.sleep(2)
        self.helpers.alerts_activities_details()

        self.activities_page.navigate_to_activities_page()
        url = self.driver.current_url()
        self.assertEqual('http://localhost:4200/activities', url, 'activities page shown')
        self.driver.quit()


    def test_no_fill_my_mission(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login('test', '258963')

        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('', ' test')
        time.sleep(2)
        alert = self.helpers.alerts_activities_details()
        assert alert == 'Http failure response for https://localhost:7216/api/Activity: 400 OK'
        self.driver.quit()


    def test_no_fill_why_i_do_this(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login('test', '258963')

        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('test', '')
        time.sleep(2)
        alert = self.helpers.alerts_activities_details()
        assert alert == 'Http failure response for https://localhost:7216/api/Activity: 400 OK'
        self.driver.quit()


    def test_no_fill(self):
        self.login_page.navigate_to_login_page()
        self.login_page.login('test', '258963')

        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('', '')
        time.sleep(2)
        alert = self.helpers.alerts_activities_details()
        assert alert == 'Http failure response for https://localhost:7216/api/Activity: 400 OK'
        self.driver.quit()

