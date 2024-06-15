import unittest

import waits.wait
from helpers.AlertsAndStrings import AgendaPageOpen, AgendaPageOpenByDropList, DaysDontMatch, ActualDate, \
 \
    TodayBtnDisable, VerifyTodayDisable, ExpectedDate, YesterdayBtnInvalidText
from helpers.Helpers import HelpersMbs
from initialize_driver import initialize_driver
from locators.agenda_menu_locators.MyAgendaPageLocators import MyAgendaPageLocators
from pages.LoginPage import LoginPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.Pages_url import PagesUrlMbs


class TestActivitiesPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.agenda_page = MyAgendaPage(self.driver)

    def test_open_page(self):
        self.login_page.success_login()
        self.agenda_page.navigate_to_agenda_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.agenda, print(AgendaPageOpen.my_string))

    def test_open_page_by_drop_list(self):
        self.login_page.success_login()
        self.agenda_page.open_agenda_drop_list()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.agenda, print(AgendaPageOpenByDropList.my_string))

    def test_today_btn_disable_default(self):
        self.login_page.success_login()
        self.agenda_page.navigate_to_agenda_page()

        HelpersMbs.scroll_to_bottom(self.driver)
        today_btn = self.driver.find_element(*MyAgendaPageLocators.TODAY_BTN)
        today_btn.get_attribute("class")

        confirm_btn_disable = HelpersMbs.is_button_disabled(self.driver, *MyAgendaPageLocators.TODAY_BTN)
        print(f"{VerifyTodayDisable.my_string} {confirm_btn_disable}")

        self.assertEqual(confirm_btn_disable, True, TodayBtnDisable.my_string)
        self.driver.quit()

    def test_verify_default_day_today(self):
        self.login_page.success_login()
        self.agenda_page.navigate_to_agenda_page()

        today_date = HelpersMbs.get_today_date_in_hebrew()
        print(ExpectedDate.my_string)

        actual_text = self.agenda_page.get_default_day()
        print(f"{ActualDate.my_string} {actual_text}")

        self.assertEqual(actual_text, today_date, DaysDontMatch.my_string)

        self.driver.quit()

    def test_verify_yesterday_btn(self):
        self.login_page.success_login()
        self.agenda_page.navigate_to_agenda_page()

        actual_date, expected_date = self.agenda_page.verify_yesterday_btn()

        print(f"{ActualDate.my_string} {actual_date}, {ExpectedDate.my_string}: {expected_date}")

        self.assertEqual(actual_date, expected_date, YesterdayBtnInvalidText.my_string)
