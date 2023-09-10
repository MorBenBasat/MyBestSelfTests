from helpers.Helpers import HelpersMbs
from locators.MyAgendaPageLocators import MyAgendaPageLocators
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.Pages_url import PagesUrlMbs
from waits.wait import wait_for_element_presence, wait_for_element_clickable
from locators.ActivitiesLocators import ActivitiesLocators


class ActivitiesPage:

    def __init__(self, driver):
        self.driver = driver
        self.helpers = HelpersMbs(driver)
        self.pageUrl = PagesUrlMbs.activities
        self.my_agenda = MyAgendaPage(self.driver)

    def navigate_to_activities_page(self):
        HelpersMbs.delay(2)
        self.helpers.navigation_to_url(self.pageUrl)

    def navigate_to_activities_page_by_drop_list(self):
        HelpersMbs.delay(1)
        self.my_agenda.open_agenda_drop_list()
        click_on_activities_page_drop_list = wait_for_element_clickable(self.driver, *ActivitiesLocators.
                                                                        DROP_LIST_ACTIVITIES_PAGE_CLICK)
        click_on_activities_page_drop_list.click()

    def navigate_to_activities_page_by_folder_icon(self):
        HelpersMbs.delay(2)
        MyAgendaPage.navigate_to_agenda_page(self.driver)
        click_on_folder_icon_btn = wait_for_element_clickable(self.driver, *MyAgendaPageLocators.
                                                              FOLDER_BTN_OPEN_ALL_ACTIVITIES)
        click_on_folder_icon_btn.click()
