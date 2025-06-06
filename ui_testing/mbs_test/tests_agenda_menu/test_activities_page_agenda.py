import time
import unittest

from helpers.AlertsAndStrings import CardDoesntAdded, ActivitiesOpen, \
    ActivityPageDropList, UpdateUserAlert
from locators.agenda_menu_locators.ActivitiesLocators import ActivitiesLocators
from pages.Agenda.ActivitiesPageAgenda import ActivitiesPage
from initialize_driver import initialize_driver
from pages.Agenda.ActivitiesDetailsPageAgenda import ActivitiesDetailsPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.activities_details_users import ValidActivityDetails
from helpers.Helpers import HelpersMbs
from waits.wait import wait_for_elements


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
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities, print(ActivitiesOpen.my_string))

    def test_open_activities_by_drop_list(self):
        self.login_page.success_login()
        self.activities_page.navigate_to_activities_page_by_drop_list()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities, print(ActivityPageDropList.my_string))

    def test_edit_btn_click_and_update(self):
        self.login_page.success_login()
        self.activities_page.navigate_to_activities_page()
        self.activities_page.edit_exist_activity()
        expected_text = UpdateUserAlert.alert

        actual_text = HelpersMbs(self.driver).update_alert_text()
        self.assertEqual(actual_text, expected_text)

    def test_verify_activity_added_to_page(self):
        self.login_page.success_login()
        self.activities_page.navigate_to_activities_page()
        HelpersMbs.scroll_to_bottom_or_up(self.driver,"DOWN")

        all_cards_before = wait_for_elements(self.driver, ActivitiesLocators.AMOUNT_OF_ACTIVITIES)
        count_before = len(all_cards_before)
        HelpersMbs.delay(1)

        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.create_activity_details(ValidActivityDetails)
        self.activities_page.navigate_to_activities_page()

        HelpersMbs.scroll_to_bottom_or_up(self.driver,"DOWN")
        HelpersMbs.delay(1)

        all_cards_after = wait_for_elements(self.driver, ActivitiesLocators.AMOUNT_OF_ACTIVITIES)
        count_after = len(all_cards_after)

        print(count_before, count_after)
        assert count_after == count_before + 1, CardDoesntAdded.my_string

        self.driver.quit()
