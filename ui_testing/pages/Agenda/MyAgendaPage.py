from helpers.Helpers import HelpersMbs
from locators.MyAgendaPageLocators import MyAgendaPageLocators
from pages.Pages_url import PagesUrlMbs
from waits.wait import wait_for_element_clickable


class MyAgendaPage:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = HelpersMbs(self.driver)
        self.pageUrl = PagesUrlMbs.agenda

    def navigate_to_agenda_page(self):
        self.helpers.navigation_to_url(self.pageUrl)
        HelpersMbs.delay(2)

    def open_agenda_drop_list(self):
        click_on_agenda_drop_list = wait_for_element_clickable(self.driver, *MyAgendaPageLocators.
                                                               CLICK_ON_AGENDA_DROP_LIST)
        click_on_agenda_drop_list.click()

    def open_activity_page_by_plus_icon(self):
        click_plus_icon = wait_for_element_clickable(self.driver, *MyAgendaPageLocators.PLUS_BTN_OPEN_ACTIVITY_DETAILS)
        click_plus_icon.click()


