import unittest
import pytest
from pages.Agenda.ActivitiesPage import ActivitiesPage
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.Agenda.ActivitiesDetailsPage import ActivitiesDetailsPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.activities_details_users import ValidActivityDetails


class TestActivitiesDetailsPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.activities_details_page = ActivitiesDetailsPage(self.driver)
        self.activities_page = ActivitiesPage(self.driver)
        self.agenda_page = MyAgendaPage(self.driver)

    @pytest.mark.smoke
    def test_success_navigation_activities_details_page(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities_details, print('Activities Details Page Open!'))
        self.driver.quit()

    def test_create_activity(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('sanitytest', 'sanity test')
        HelpersMbs.delay(2)
        self.helpers.alerts_activities_details()

        self.activities_page.navigate_to_activities_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities, 'activities page shown')

        self.driver.quit()

    def test_no_fill_my_activity(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('', ' test')
        HelpersMbs.delay(2)
        alert = self.helpers.alerts_activities_details()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצרה משימה')
        self.driver.quit()

    def test_no_fill_why_i_do_this(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('test', ' ')
        HelpersMbs.delay(2)
        alert = self.helpers.alerts_activities_details()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצרה משימה')
        self.driver.quit()

    def test_no_fill_activities_details_fields(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('', '')
        HelpersMbs.delay(2)
        alert = self.helpers.alerts_activities_details()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצרה משימה')
        self.driver.quit()

    def test_open_activities_details_by_drop_list(self):
        self.login_page.success_login()
        self.agenda_page.open_agenda_drop_list()
        self.activities_details_page.navigate_to_activities_details_page_by_drop_list()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities_details,
                         print('Activities Details Page Open By '
                               'Drop List!'))
        self.driver.quit()

    def test_open_activities_details_by_plus_btn(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page_by_plus_btn()
        HelpersMbs.delay(2)
        self.assertNotEqual(self.driver.current_url, PagesUrlMbs.login, print('Activities Details Page Open By '
                                                                              'Plus Icon'))
        self.driver.quit()

    def verify_match_creating_activity_details(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        HelpersMbs.delay(2)
