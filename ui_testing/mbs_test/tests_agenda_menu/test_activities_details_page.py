import unittest
from datetime import datetime

from locators.agenda_menu_locators.ActivitiesDetailsLocators import ActivitiesDetailsLocators
from pages.Agenda.ActivitiesPage import ActivitiesPage
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.Agenda.ActivitiesDetailsPage import ActivitiesDetailsPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.activities_details_users import ValidActivityDetails, NoFillActivityName, NoFillWhyImDoingThis, \
    NoFillField
from waits.wait import wait_for_element_visibility


class TestActivitiesDetailsPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.activities_details_page = ActivitiesDetailsPage(self.driver)
        self.activities_page = ActivitiesPage(self.driver)
        self.agenda_page = MyAgendaPage(self.driver)

    def test_success_navigation_activities_details_page(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities_details,
                         print('Activities Details Page Open!'))
        self.driver.quit()

    def test_create_activity(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.create_activity_details(ValidActivityDetails)
        HelpersMbs.delay(1)
        print(self.helpers.alerts_display())
        self.activities_page.navigate_to_activities_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities, 'activities page shown')
        self.driver.quit()

    def test_no_fill_my_activity(self):
        self.activities_details_page.navigate_to_activities_details_page()
        confirm_btn_disable = HelpersMbs.is_disabled(self.driver, ActivitiesDetailsLocators.
                                                     ACTIVITIES_DETAILS_CONFIRM_BTN)

        self.activities_details_page.create_activity_details(NoFillActivityName)
        self.assertEqual(confirm_btn_disable, True, print("כפתור מוצג לא לחיץ ללא מילוי שם משימה"))

        self.driver.quit()

    def test_no_fill_why_i_do_this(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.create_activity_details(NoFillWhyImDoingThis)

        confirm_btn_able = HelpersMbs.is_enabled(self.driver, ActivitiesDetailsLocators.ACTIVITIES_DETAILS_CONFIRM_BTN)

        self.assertEqual(confirm_btn_able, True, print("כפתור מוצג לחיץ לאחר אי מילוי מדוע אני עושה את זה"))

        self.driver.quit()

    def test_no_fill_activities_details_fields(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.create_activity_details(NoFillField)
        confirm_btn_disable = HelpersMbs.is_disabled(self.driver, ActivitiesDetailsLocators.
                                                     ACTIVITIES_DETAILS_CONFIRM_BTN)

        self.assertEqual(confirm_btn_disable, True, print("כפתור מוצג לא לחיץ"))

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
        HelpersMbs.delay(1)
        self.assertNotEqual(self.driver.current_url, PagesUrlMbs.login, print('Activities Details Page Open By '
                                                                              'Plus Icon'))
        self.driver.quit()

    def test_verify_match_creating_activity_details(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        HelpersMbs.delay(1)

        self.driver.quit()

    def test_choose_time_by_arrows(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.select_time_by_arrows()
        print("All arrows has been clicked!")
        self.driver.quit()

    def test_choose_day_and_remove(self):
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.select_day_and_remove(ValidActivityDetails)
        assert ActivitiesDetailsLocators.DAY_IN_DAYS_FIELD not in ActivitiesDetailsLocators.DAYS_FIELD
        print("Day successfully removed!")

    def test_click_all_day_radio_btn(self):
        self.activities_details_page.navigate_to_activities_details_page()
        days_field = self.activities_details_page.radio_all_days_click(ValidActivityDetails)

        days_text = days_field.text
        print('days_text: ' + days_text)

        days_list = days_text.split('\n')
        print(f"days_list:  {len(days_list)}, success ")

        HelpersMbs.delay(1)
        assert len(days_list) == 7, f"Expected 7 days, but found {len(days_list)} days:\n{days_list}"

    def test_verify_not_exist_day(self):
        self.activities_details_page.navigate_to_activities_details_page()
        expected_text = 'No results found'
        actual_text = self.activities_details_page.write_unexist_day_in_day_search(expected_text)
        self.assertEqual(actual_text, expected_text, print('טקסט דרישת מילוי מופיע'))

    def test_verify_mandatory_text_hour_field(self):
        self.activities_details_page.navigate_to_activities_details_page()
        expected_text = 'נא מלא שדה זה לפני שליחה'
        actual_text = self.activities_details_page.verify_hour_mandatory_text(expected_text)
        self.assertEqual(actual_text, expected_text)

    def test_verify_mandatory_text_my_activity(self):
        self.activities_details_page.navigate_to_activities_details_page()
        expected_text = 'נא מלא שדה זה לפני שליחה'
        actual_text = self.activities_details_page.verify_my_activity_mandatory_text(expected_text)
        self.assertEqual(actual_text, expected_text)

    def test_verify_mandatory_days_text(self):
        self.activities_details_page.navigate_to_activities_details_page()
        expected_text = 'נא מלא שדה זה לפני שליחה'
        actual_text = self.activities_details_page.verify_day_mandatory_text(expected_text)
        self.assertEqual(actual_text, expected_text)

    def test_verify_activity_name_equals_green_alert_text(self):
        self.activities_details_page.navigate_to_activities_details_page()
        green_alert_text = self.activities_details_page.green_creation_alert(ValidActivityDetails)

        assert ValidActivityDetails.activity_name in green_alert_text
        print(f" מופיעה בהערת יצירה {ValidActivityDetails.activity_name}משימה בשם : ")

    from datetime import datetime

    def test_verify_clear_fields_navigate_drop_list(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page_by_drop_list()

        activity_name = wait_for_element_visibility(self.driver, *ActivitiesDetailsLocators.MY_ACTIVITY)
        activity_description = wait_for_element_visibility(self.driver, *ActivitiesDetailsLocators.ACTIVITY_DESCRIPTION)
        hour_text = wait_for_element_visibility(self.driver, *ActivitiesDetailsLocators.HOUR_FIELD)

        activity_name_text = activity_name.text
        activity_description_text = activity_description.text
        hour_text = hour_text.text

        assert activity_name_text == "", "Activity name field is not clear"
        assert activity_description_text == "", "Activity description field is not clear"
        assert hour_text == "", "Hour field is not clear"

        current_time = datetime.now().strftime("%H:%M")
        assert hour_text == current_time, f"Hour field does not display current time. Expected: {current_time}, Actual: {hour_text}"

        print("clear!")
