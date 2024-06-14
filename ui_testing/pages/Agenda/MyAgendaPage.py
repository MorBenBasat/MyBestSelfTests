from selenium.webdriver import ActionChains

from helpers.Helpers import HelpersMbs
from locators.agenda_menu_locators.MyAgendaPageLocators import MyAgendaPageLocators
from pages.Pages_url import PagesUrlMbs
from waits.wait import wait_for_element_clickable, wait_for_element_presence


class MyAgendaPage:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = HelpersMbs(self.driver)
        self.pageUrl = PagesUrlMbs.agenda

    def navigate_to_agenda_page(self):
        self.helpers.navigation_to_url(self.pageUrl)
        HelpersMbs.delay(2)

    def open_agenda_drop_list(self):
        HelpersMbs.delay(1)
        open_agenda_drop_list_element = wait_for_element_presence(self.driver,
                                                                  *MyAgendaPageLocators.OPEN_AGENDA_DROP_LIST)
        action = ActionChains(self.driver)
        action.move_to_element(open_agenda_drop_list_element).perform()
        HelpersMbs.delay(1)

    def open_activity_page_by_plus_icon(self):
        plus_icon = wait_for_element_clickable(self.driver, *MyAgendaPageLocators.PLUS_BTN_OPEN_ACTIVITY_DETAILS)
        plus_icon.click()

    def get_default_day(self):
        day_text_field= wait_for_element_presence(self.driver, *MyAgendaPageLocators.DAY_TEXT)
        return day_text_field.text

    def get_title_name_agenda(self):
        title_name = wait_for_element_presence(self.driver, *MyAgendaPageLocators.DAY_TEXT)
        return title_name.text

