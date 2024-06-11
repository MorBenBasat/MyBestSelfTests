import unittest
from locators.agenda_menu_locators.ActivitiesLocators import ActivitiesLocators
from pages.Agenda.ActivitiesPage import ActivitiesPage
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.Agenda.ActivitiesDetailsPage import ActivitiesDetailsPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.activities_details_users import ValidActivityDetails


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
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities, print('Activities page opens properly'))

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
        assert count_after == count_before + 1, "New activity was not added successfully"

    # def test_add_to_activity_btn_verify_btn_name_change(self):
    #     self.login_page.success_login()
    #     self.activities_page.navigate_to_activities_page()
    #
    #     self.activities_page.click_on_add_activity_to_agenda()
