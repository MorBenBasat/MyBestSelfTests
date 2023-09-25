from selenium.webdriver import ActionChains, Keys
from helpers.Helpers import HelpersMbs
from locators.MyAgendaPageLocators import MyAgendaPageLocators
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.Pages_url import PagesUrlMbs
from waits.wait import wait_for_element_presence, wait_for_element_clickable
from locators.ActivitiesDetailsLocators import ActivitiesDetailsLocators
from pages.LoginPage import LoginPage


class ActivitiesDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = HelpersMbs(self.driver)
        self.pageUrl = PagesUrlMbs.activities_details
        self.my_agenda = MyAgendaPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.action_chains = ActionChains(self.driver)

    def navigate_to_activities_details_page(self):
        self.login_page.success_login()
        HelpersMbs.delay(1)
        self.helpers.navigation_to_url(self.pageUrl)

    def navigate_to_activities_details_page_by_drop_list(self):
        HelpersMbs.delay(1)
        click_on_activities_page_drop_list = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.
                                                                        DROP_LIST_ACTIVITIES_DETAILS_PAGE_CLICK)
        HelpersMbs.delay(2)

        click_on_activities_page_drop_list.click()

    def navigate_to_activities_details_page_by_plus_btn(self):
        HelpersMbs.delay(1)
        self.my_agenda.navigate_to_agenda_page()

        click_on_plus_btn = wait_for_element_clickable(self.driver,
                                                       *MyAgendaPageLocators.PLUS_BTN_OPEN_ACTIVITY_DETAILS)
        click_on_plus_btn.click()

    def fill_all_activities_details(self, ActivityDetails):
        my_activity_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.MY_ACTIVITY)
        my_activity_field.click
        HelpersMbs.delay(2)
        my_activity_field.send_keys(ActivityDetails.activity_name)

        why_i_do_this_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.WHY_I_DO_THIS)
        why_i_do_this_field.send_keys(ActivityDetails.activity_text)

        hour_field_open = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        hour_field_open.click()
        HelpersMbs.delay(1)
        for _ in range(5):
            hour_field_open.send_keys(Keys.BACK_SPACE)
        HelpersMbs.delay(1)
        fill_hour_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        fill_hour_field.send_keys(ActivityDetails.hour)

        random_click = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.WHY_I_DO_THIS)
        random_click.click()
        HelpersMbs.delay(2)

        days_field_open = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.DAYS_FIELD)
        days_field_open.click()
        HelpersMbs.delay(2)

        days_field_selection = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.DAYS_SEARCH_FIELD)
        days_field_selection.send_keys('ראשון')
        HelpersMbs.delay(2)

        click_on_day = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.SUNDAY_BTN)
        click_on_day.click()

        random_click.click()

        confirm_btn = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.CONFIRM_BTN)

        confirm_btn.click()
