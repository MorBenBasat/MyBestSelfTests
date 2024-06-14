import unittest

from helpers.AlertsAndStrings import AgendaPageOpen, AgendaPageOpenByDropList
from helpers.Helpers import HelpersMbs
from initialize_driver import initialize_driver
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
        self.assertEqual(self.driver.current_url, PagesUrlMbs.activities, print(AgendaPageOpen.my_string))

    def test_open_page_by_drop_list(self):
        self.login_page.success_login()
        self.agenda_page.open_agenda_drop_list()
        self.assertEqual(self.driver.current_url, PagesUrlMbs.agenda, print(AgendaPageOpenByDropList.my_string))

    def test_verify_default_day_today(self):
        self.login_page.success_login()
        self.agenda_page.navigate_to_agenda_page()
        expected_text = "123"  # Access the string value
        actual_text = self.agenda_page.get_default_day()
        print(f"Expected: {expected_text}, Actual: {actual_text}")  # Add a print statement for debugging
        self.assertEqual(actual_text, expected_text)
        self.driver.quit()
