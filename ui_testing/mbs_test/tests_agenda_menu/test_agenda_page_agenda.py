import unittest
from datetime import datetime

from helpers.AlertsAndStrings import AgendaPageOpen, AgendaPageOpenByDropList
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
        # Set the locale to Hebrew (Israel)
        locale.setlocale(locale.LC_TIME, 'he_IL.utf8')  # Adjust if needed based on your system's locale settings

        self.login_page.success_login()
        self.agenda_page.navigate_to_agenda_page()

        # Get today's date formatted as "14 ביוני 2024"
        today_date = datetime.now().strftime('%d ב%B %Y')

        # Print today's date for debugging
        print(f"Expected date: {today_date}")

        # Fetch the actual day text from the page
        actual_text = self.agenda_page.get_default_day()

        # Print actual day text for debugging
        print(f"Actual day text: {actual_text}")

        # Assert that the actual day text matches today's date
        self.assertEqual(today_date, actual_text, "The displayed day does not match today's date")

        self.driver.quit()