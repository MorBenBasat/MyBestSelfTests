import time

from helpers.Helpers import HelpersMbs
from locators.agenda_menu_locators.ActivitiesDetailsLocators import ActivitiesDetailsLocators
from locators.agenda_menu_locators.MyAgendaPageLocators import MyAgendaPageLocators
from pages.Agenda.ActivitiesDetailsPageAgenda import fil
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.Pages_url import PagesUrlMbs
from waits.wait import wait_for_element_presence, wait_for_element_clickable
from locators.agenda_menu_locators.ActivitiesLocators import ActivitiesLocators


class ActivitiesPage:

    def __init__(self, driver):
        self.driver = driver
        self.helpers = HelpersMbs(driver)
        self.pageUrl = PagesUrlMbs.activities
        self.my_agenda = MyAgendaPage(self.driver)

    def navigate_to_activities_page(self):
        self.helpers.navigation_to_url(self.pageUrl)
        HelpersMbs.delay(1)

    def navigate_to_activities_page_by_drop_list(self):
        HelpersMbs.delay(2)
        self.my_agenda.open_agenda_drop_list()
        click_on_activities_page_drop_list = wait_for_element_clickable(self.driver, *ActivitiesLocators.
                                                                        DROP_LIST_ACTIVITIES_PAGE_CLICK)
        click_on_activities_page_drop_list.click()
        HelpersMbs.delay(2)

    def navigate_to_activities_page_by_folder_icon(self):
        HelpersMbs.delay(1)
        MyAgendaPage.navigate_to_agenda_page(self.driver)
        click_on_folder_icon_btn = wait_for_element_clickable(self.driver, *MyAgendaPageLocators.
                                                              FOLDER_BTN_OPEN_ALL_ACTIVITIES)
        click_on_folder_icon_btn.click()

    def edit_exist_activity(self):
        edit_btn = wait_for_element_clickable(self.driver, *ActivitiesLocators.EDIT_ACTIVITY_BTN)
        edit_btn.click()
        edit_the_activity = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.MY_ACTIVITY_FIELD)
        edit_the_activity.clear()
        HelpersMbs.delay(1)

        edit_the_activity.send_keys(HelpersMbs.random_string())
        confirm_btn = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.CONFIRM_BTN)
        confirm_btn.click()
        HelpersMbs.delay(1)

    def verify_activity_creation(self, ActivityDetails):
        self.driver.create_activity_details(ActivityDetails)
