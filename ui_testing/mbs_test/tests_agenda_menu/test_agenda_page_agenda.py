import unittest

from helpers.AlertsAndStrings import AgendaPageOpen, AgendaPageOpenByDropList, DaysDontMatch,  \
 \
    TodayBtnDisable, VerifyTodayDisable, YesterdayBtnInvalidText, DateBeforeBtnYesterday
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

        HelpersMbs.scroll_to_bottom_or_up(self.driver, "DOWN")
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
        print(f"today date : {today_date})")

        actual_day = self.agenda_page.get_default_day()
        print(f"Actual day text : {actual_day}")

        self.assertEqual(actual_day, today_date, DaysDontMatch.my_string)

        self.driver.quit()

    def test_verify_yesterday_btn(self):
        self.login_page.success_login()
        self.agenda_page.navigate_to_agenda_page()

        expected_date, date_before_click_yesterday_btn = self.agenda_page.verify_yesterday_btn()
        print(f"{DateBeforeBtnYesterday.my_string} {date_before_click_yesterday_btn}")
        print(f"Day after click {expected_date}")
        self.assertNotEqual(date_before_click_yesterday_btn, expected_date, YesterdayBtnInvalidText.my_string)

    def test_verify_tomorrow_btn(self):
        pass
