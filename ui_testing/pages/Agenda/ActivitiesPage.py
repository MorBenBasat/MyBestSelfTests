from helpers.Helpers import HelpersMbs
from locators.ActivitiesDetailsLocators import ActivitiesDetailsLocators
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
        HelpersMbs.delay(1)
        self.helpers.navigation_to_url(self.pageUrl)

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

    def edit_exist_activity(self,text_fill):
        edit_btn = wait_for_element_clickable(self.driver, *ActivitiesLocators.EDIT_ACTIVITY_BTN)
        edit_btn.click()
        edit_the_activity = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.MY_ACTIVITY)
        edit_the_activity.clear()
        HelpersMbs.delay(1)
        edit_the_activity.send_keys(text_fill)
        confirm_btn = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.CONFIRM_BTN)
        confirm_btn.click()
        HelpersMbs.delay(1)

    def update_alert(self, expected_text, text_fill):
        self.edit_exist_activity(text_fill)
        alert_text = wait_for_element_presence(self.driver, *ActivitiesLocators.ACTIVATE_ALERT_CONFIRM)
        if alert_text.text == expected_text:
            print('הטקסט המצופה', expected_text)
        else:
            print('Text is not as expected. Actual text:', alert_text.text)
        return alert_text.text
