import unittest
import pytest
from pages.Agenda.ActivitiesPage import ActivitiesPage
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.Agenda.ActivitiesDetailsPage import ActivitiesDetailsPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.login_users import SuccessLoginUser, InvalidLogin


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
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(SuccessLoginUser.login, SuccessLoginUser.password)
        self.activities_details_page.navigate_to_activities_details_page()
        url = self.driver.current_url
        self.assertEqual(PagesUrlMbs.activities_details, url, 'Activities Details Page Open!')
        self.driver.quit()

    @pytest.mark.smokeee
    def test_create_activity(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(SuccessLoginUser.login, SuccessLoginUser.password)
        HelpersMbs.delay(2)

        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('sanitytest', 'sanity test')
        HelpersMbs.delay(2)
        self.helpers.alerts_activities_details()

        self.activities_page.navigate_to_activities_page()
        url = self.driver.current_url()
        self.assertEqual(PagesUrlMbs.activities, url, 'activities page shown')
        self.driver.quit()

    def test_no_fill_my_activity(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(InvalidLogin.login, InvalidLogin.password)

        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('', ' test')
        HelpersMbs.delay(2)
        alert = self.helpers.alerts_activities_details()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצרה משימה')

        self.driver.quit()

    def test_no_fill_why_i_do_this(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(SuccessLoginUser.login, SuccessLoginUser.password)

        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('test', ' ')
        HelpersMbs.delay(2)
        alert = self.helpers.alerts_activities_details()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצרה משימה')
        self.driver.quit()

    def test_no_fill_activities_details_fields(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(SuccessLoginUser.login, SuccessLoginUser.password)

        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details('', '')
        HelpersMbs.delay(2)
        alert = self.helpers.alerts_activities_details()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצרה משימה')
        self.driver.quit()

    def test_open_activities_details_by_drop_list(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(SuccessLoginUser.login, SuccessLoginUser.password)
        HelpersMbs.delay(2)
        self.agenda_page.open_agenda_drop_list()
        url = self.driver.current_url
        self.activities_details_page.navigate_to_activities_details_page_by_drop_list()
        self.assertNotEqual(PagesUrlMbs.activities_details, url, print('Activities Details Page Open By '
                                                                       'Drop List!'))
        self.driver.quit()

    def test_open_activities_details_by_plus_btn(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(SuccessLoginUser.login, SuccessLoginUser.password)
        HelpersMbs.delay(2)
        url = self.driver.current_url
        self.activities_details_page.navigate_to_activities_details_page_by_plus_btn()
        self.assertNotEqual(PagesUrlMbs.activities_details, url, print('Activities Details Page Open By '
                                                                       'Folder Icon'))
        self.driver.quit()

    def verify_match_creating_activity_details(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.login_page.login(SuccessLoginUser.login, SuccessLoginUser.password)
        HelpersMbs.delay(2)
        self.activities_details_page.navigate_to_activities_details_page()
        HelpersMbs.delay(2)

