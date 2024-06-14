import unittest
from datetime import datetime

from helpers.AlertsAndStrings import AgendaPageOpen, AgendaPageOpenByDropList, DaysDontMatch, ExpectedDate, ActualDate
from helpers.Helpers import HelpersMbs
from initialize_driver import initialize_driver
from pages.LoginPage import LoginPage
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.Pages_url import PagesUrlMbs
import locale


class TestActivitiesPage(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.agenda_page = MyAgendaPage(self.driver)

    def test_open_page(self):
        self.login_page.success_login()
        self.agenda_page.navigate_to_agenda_page()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities, print(AgendaPageOpen.my_string))

    def test_open_page_by_drop_list(self):
        self.login_page.success_login()
        self.agenda_page.open_agenda_drop_list()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.agenda, print(AgendaPageOpenByDropList.my_string))

    def test_verify_default_day_today(self):
        self.login_page.success_login()
        self.agenda_page.navigatce_to_agenda_page()

        today_date = HelpersMbs.get_today_date_in_hebrew()
        print(ExpectedDate.my_string)

        actual_text = self.agenda_page.get_default_day()
        print(f"{ActualDate.my_string} {actual_text}")

        self.assertEqual(actual_text, today_date, DaysDontMatch.my_string)

        self.driver.quit()


