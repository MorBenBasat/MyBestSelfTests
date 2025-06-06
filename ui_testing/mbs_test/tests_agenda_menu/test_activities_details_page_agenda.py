import unittest
from datetime import datetime

from helpers.AlertsAndStrings import MandatoryFieldText, NoResultText, NewActivityCreate, DropListClearField, \
    DayRemoved, DetailsPageAgendaOpenDropList, DisableBtn, AbleBtn, DaysText, ActivitiesOpen, TimeDontChange

from locators.agenda_menu_locators.ActivitiesDetailsLocators import ActivitiesDetailsLocators
from pages.Agenda.ActivitiesPageAgenda import ActivitiesPage
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.Agenda.ActivitiesDetailsPageAgenda import ActivitiesDetailsPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from test_users.activities_details_users import ValidActivityDetails, NoFillActivityName, NoFillWhyImDoingThis, \
    NoFillField


class TestActivitiesDetailsPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.activities_details_page = ActivitiesDetailsPage(self.driver)
        self.activities_page = ActivitiesPage(self.driver)
        self.agenda_page = MyAgendaPage(self.driver)

    def test_success_navigation_activities_details_page(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities_details,
                         print(DetailsPageAgendaOpen.my_string))
        self.driver.quit()

    def test_create_activity(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.create_activity_details(ValidActivityDetails)
        HelpersMbs.delay(1)
        print(self.helpers.alerts_display())
        self.activities_page.navigate_to_activities_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities,ActivitiesOpen.my_string)
        self.driver.quit()

    def test_no_fill_my_activity(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        confirm_btn_disable = HelpersMbs.is_disabled(self.driver, ActivitiesDetailsLocators.
                                                     ACTIVITIES_DETAILS_CONFIRM_BTN)

        self.activities_details_page.fill_all_activities_details_without_btn_click(NoFillActivityName)
        self.assertEqual(confirm_btn_disable, True, print(DisableBtn.my_string))

        self.driver.quit()

    def test_no_fill_why_i_do_this(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details_without_btn_click(NoFillWhyImDoingThis)

        confirm_btn_disable = HelpersMbs.is_disabled(self.driver, ActivitiesDetailsLocators.
                                                     ACTIVITIES_DETAILS_CONFIRM_BTN)

        self.assertEqual(confirm_btn_disable, False, print(AbleBtn.my_string))

        self.driver.quit()

    def test_no_fill_activities_details_fields(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_all_activities_details_without_btn_click(NoFillField)
        confirm_btn_disable = HelpersMbs.is_disabled(self.driver, ActivitiesDetailsLocators.
                                                     ACTIVITIES_DETAILS_CONFIRM_BTN)

        self.assertEqual(confirm_btn_disable, True, print(DisableBtn.my_string))

        self.driver.quit()

    def test_open_activities_details_by_drop_list(self):
        self.login_page.success_login()
        self.agenda_page.open_agenda_drop_list()
        self.activities_details_page.navigate_to_activities_details_page_by_drop_list()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities_details,
                         print(DetailsPageAgendaOpenDropList.my_string))

        self.driver.quit()

    def test_open_activities_details_by_plus_btn(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page_by_plus_btn()
        HelpersMbs.delay(1)
        self.assertNotEqual(self.driver.current_url, PagesUrlMbs.login, print(DetailsPageAgendaOpenDropList.my_string))
        self.driver.quit()

    def test_verify_match_creating_activity_details(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        HelpersMbs.delay(1)
        self.driver.quit()

    def test_choose_time_by_arrows_one_hour_up(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        initial_time = self.activities_details_page.get_time_value()

        self.activities_details_page.select_time_by_arrows()

        final_time = self.activities_details_page.get_time_value()

        print(final_time, initial_time)
        self.assertNotEqual(initial_time, final_time, TimeDontChange.my_string)

        self.driver.quit()

    def test_choose_day_and_remove(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.select_day_and_remove(ValidActivityDetails)
        assert ActivitiesDetailsLocators.DAY_IN_DAYS_FIELD not in ActivitiesDetailsLocators.DAYS_FIELD
        print(DayRemoved.alert)
        self.driver.quit()

    def test_click_all_day_radio_btn(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        days_field = self.activities_details_page.radio_all_days_click(ValidActivityDetails)

        days_text = days_field.text
        print(DaysText.my_string + days_text)

        days_list = days_text.split('\n')
        print(f"days_list:  {len(days_list)}, success ")

        HelpersMbs.delay(1)
        assert len(days_list) == 7, f"Expected 7 days, but found {len(days_list)} days:\n{days_list}"
        self.driver.quit()

    def test_verify_not_exist_day(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        expected_text = NoResultText.alert
        actual_text = self.activities_details_page.write_unexist_day_in_day_search(expected_text)
        self.assertEqual(actual_text, expected_text)
        self.driver.quit()

    def test_verify_mandatory_text_hour_field(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        expected_text = MandatoryFieldText.my_string
        actual_text = self.activities_details_page.verify_hour_mandatory_text(expected_text)
        self.assertEqual(actual_text, expected_text)
        self.driver.quit()

    def test_verify_mandatory_text_my_activity(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        expected_text = MandatoryFieldText.my_string
        actual_text = self.activities_details_page.verify_my_activity_mandatory_text(expected_text)
        self.assertEqual(actual_text, expected_text)

    def test_verify_mandatory_days_text(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        expected_text = MandatoryFieldText.alert
        actual_text = self.activities_details_page.verify_day_mandatory_text(expected_text)
        self.assertEqual(actual_text, expected_text)
        self.driver.quit()

    def test_verify_activity_name_equals_green_alert_text(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        green_alert_text = self.activities_details_page.green_creation_alert(ValidActivityDetails)

        assert ValidActivityDetails.activity_name in green_alert_text
        print(NewActivityCreate.my_string)
        self.driver.quit()

    def test_verify_clear_fields_navigate_drop_list(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page_by_drop_list()
        hour_text, min_text = self.activities_details_page.verify_clear_fields_navigate_drop_list()

        current_time = datetime.now().strftime("%H:%M")
        expected_time = f"{current_time[:2]}:{min_text}"

        assert hour_text == current_time[:2], "Hour error"
        assert min_text == current_time[3:], "Minute error"
        assert expected_time == f"{current_time[:2]}:{min_text}", "Time error"

        print(DropListClearField.my_string)
        self.driver.quit()

    def test_verify_day_selected(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        self.activities_details_page.fill_fields_until_day_field(NoFillField)
        self.activities_details_page.select_day_radio_button("שלישי")

    def test_delete_day(self):
        self.login_page.success_login()
        self.activities_details_page.navigate_to_activities_details_page()
        days_field = self.activities_details_page.add_and_delete_day(NoFillField)

        days_text = days_field.text
        print('days selected ' + '[' + days_text + ']')

        days_list = days_text.split('\n')
        print(f"days_length: {len(days_list)} #this is not day this is placeholder")

        HelpersMbs.delay(1)
        assert "באיזה ימים זה קורה" in days_text
        self.driver.quit()
