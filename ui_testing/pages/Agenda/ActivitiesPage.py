import time

from selenium.webdriver.common.by import By

from helpers.Helpers import HelpersMbs
from pages.Pages_url import PagesUrlMbs
from waits.wait import wait_for_element_presence, wait_for_element_clickable
from locators.ActivitiesLocators import ActivitiesLocators


class ActivitiesPage:

    def __init__(self, driver):
        self.driver = driver
        self.helpers = HelpersMbs(driver)
        self.pageUrl = PagesUrlMbs.activities_details

    def open_activity_details_page_by_icon_by_drop_list(self):
        self.helpers.navigation_to_url(self.pageUrl)

    def open_activity_details_page_by_icon(self):
        click_on_create_activity = wait_for_element_clickable(self.driver, *ActivitiesLocators.CLICK_TO_CREATE_ACTIVITY_BY_IC0N_BTN)
        click_on_create_activity.click()







