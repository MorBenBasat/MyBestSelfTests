import unittest

from pages.Agenda.ActivitiesPage import ActivitiesPage
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.Agenda.ActivitiesDetailsPage import ActivitiesDetailsPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.activities_details_users import TestActivityDetailsUsers, ValidActivityDetails


class TestActivitiesPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.activities_details_page = ActivitiesDetailsPage(self.driver)
        self.activities_page = ActivitiesPage(self.driver)
        self.agenda_page = MyAgendaPage(self.driver)

    def test_success_navigation_activities_page(self):
        self.login_page.success_login()
        self.activities_page.navigate_to_activities_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities, print('Activities page opens propelry'))

    def test_open_activities_by_drop_list(self):
        self.login_page.success_login()
        self.activities_page.navigate_to_activities_page_by_drop_list()
        self.assertNotEqual(self.driver.current_url, PagesUrlMbs.login, print('Activities Details Page Open By Drop '
                                                                              'List'))

    def test_edit_btn_click_and_update(self):
        self.login_page.success_login()
        self.activities_page.navigate_to_activities_page()
        text_fill = "new text"
        expected_text = f"עדכון פריט סדר יום\nפריט סדר יום: {text_fill} התעדכן בהצלחה"
        actual_text = self.activities_page.update_alert(expected_text, text_fill)

        self.assertEqual(actual_text, expected_text)

    def test_verify_field_values_on_last_card(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.create_activity_details(ValidActivityDetails)
        self.activities_page.navigate_to_activities_page()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Verify field values on the last card
        activity_name_text, activity_text_text, hour_text, day_text = self.activities_page.verify_field_values_on_card()

        valid_activity_details = TestActivityDetailsUsers(ValidActivityDetails.activity_name,
                                                          ValidActivityDetails.activity_text,
                                                          ValidActivityDetails.hour,
                                                          ValidActivityDetails.day)

        # Assert the details
        assert valid_activity_details.activity_name == activity_name_text
        assert valid_activity_details.activity_text == activity_text_text
        assert valid_activity_details.hour == hour_text
        assert valid_activity_details.day == day_text
