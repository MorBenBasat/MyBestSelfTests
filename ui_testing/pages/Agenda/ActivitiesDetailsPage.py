import time

from selenium.webdriver.common.by import By

from helpers.Helpers import HelpersMbs
from pages.pages_url import PagesUrlMbs
from waits.wait import wait_for_element_presence, wait_for_element_clickable
from locators.ActivitiesDetailsLocators import ActivitiesDetailsLocators
from pages.pages_url import PagesUrl


class ActivitiesDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = HelpersMbs(self.driver)
        self.pageUrl = PagesUrlMbs.activities_details

    def navigate_to_activities_details_page(self):
        self.helpers.navigation_to_url(self.pageUrl)

    def fill_all_activities_details(self, my_mission, why_i_do_this):
        my_mission_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.MY_MISSION)
        my_mission_field.send_keys(my_mission)

        why_i_do_this_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.WHY_I_DO_THIS)
        why_i_do_this_field.send_keys(why_i_do_this)

        hour_field_open = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        hour_field_open.click()
        time.sleep(2)
        hour_up_arrow = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.HOUR_ARROW_UP)
        hour_up_arrow.click()

        random_click = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.WHY_I_DO_THIS)
        random_click.click()

        days_field_open = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.DAYS_FIELD)
        days_field_open.click()
        time.sleep(2)

        days_field_selection = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.MONDAY_BTN)
        days_field_selection.click()

        random_click.click()

        confirm_btn = self.driver.find_element(By.XPATH, '/html/body/app-root/div/div['
                                                         '2]/app-activities-details/div/p-button/button')

        confirm_btn.click()
