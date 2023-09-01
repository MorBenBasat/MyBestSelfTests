import time

from selenium.webdriver.common.by import By

from helpers.Helpers import HelpersMbs
from pages.pages_url import PagesUrlMbs
from waits.wait import wait_for_element_presence, wait_for_element_clickable
from locators.ActivitiesLocators import ActivitiesLocators


class ActivitiesPage:

    def __init__(self, driver):
        self.driver = driver
        self.helpers = HelpersMbs(driver)
        self.pageUrl = PagesUrlMbs.activities_details

    def navigate_to_activities_page(self):
        self.helpers.navigation_to_url(self.pageUrl)
