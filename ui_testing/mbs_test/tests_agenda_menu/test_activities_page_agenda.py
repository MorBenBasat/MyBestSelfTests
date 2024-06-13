import unittest

from helpers.AlertsAndStrings import DisableBtn, ActivityPageAgendaDropList, AgendaPagePageOpen, CardDoesntAdded
from locators.agenda_menu_locators.ActivitiesLocators import ActivitiesLocators
from locators.agenda_menu_locators.MyAgendaPageLocators import MyAgendaPageLocators
from pages.Agenda.ActivitiesPageAgenda import ActivitiesPage
from initialize_driver import initialize_driver
from pages.Agenda.ActivitiesDetailsPageAgenda import ActivitiesDetailsPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.activities_details_users import ValidActivityDetails
from helpers.Helpers import HelpersMbs


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
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities, print(AgendaPagePageOpen))

    def test_open_activities_by_drop_list(self):
        self.login_page.success_login()
        self.activities_page.navigate_to_activities_page_by_drop_list()
        self.assertNotEqual(self.driver.current_url, PagesUrlMbs.login, print(ActivityPageAgendaDropList))

    def test_edit_btn_click_and_update(self):
        self.login_page.success_login()
        self.activities_page.navigate_to_activities_page()
        expected_text = f"עדכון פריט סדר יום\nפריט סדר יום: {HelpersMbs.random_string()} התעדכן בהצלחה"
        self.activities_page.edit_exist_activity()

        actual_text = HelpersMbs(self.driver).update_alert_text()

        self.assertEqual(actual_text, expected_text)

    def test_verify_activity_added_to_page(self):
        self.login_page.success_login()
        self.activities_page.navigate_to_activities_page()

        all_cards_before = self.driver.find_elements(*ActivitiesLocators.ALL_CARDS)  #
        count_before = len(all_cards_before)

        self.activities_details_page.navigate_to_activities_details_page()

        self.activities_details_page.create_activity_details(ValidActivityDetails)
        self.activities_page.navigate_to_activities_page()

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        HelpersMbs.delay(2)

        all_cards_after = self.driver.find_elements(*ActivitiesLocators.ALL_CARDS)
        count_after = len(all_cards_after)

        print(count_before, count_after)
        assert count_after == count_before + 1,CardDoesntAdded

    def test_today_btn_disable_default(self):
        self.login_page.success_login()
        self.agenda_page.navigate_to_agenda_page()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Fetch the button element
        btn = self.driver.find_element(*MyAgendaPageLocators.TODAY_BTN)
        btn_class = btn.get_attribute("class")
        print(f"Button class attribute: {btn_class}")

        confirm_btn_disable = HelpersMbs.is_disabled(self.driver, MyAgendaPageLocators.TODAY_BTN)
        print(f"Is button disabled: {confirm_btn_disable}")

        self.assertEqual(confirm_btn_disable, True, DisableBtn )
        self.driver.quit()
