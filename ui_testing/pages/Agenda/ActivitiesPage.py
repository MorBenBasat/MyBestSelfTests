import time

from selenium.webdriver.common.by import By

from helpers.Helpers import HelpersMbs
from pages.pages_url import PagesUrl
from waits.wait import wait_for_element_presence, wait_for_element_clickable
from locators.ActivitiesLocators import ActivitiesLocators


class ActivitiesPage:

    def __init__(self, driver):
        self.driver = driver
        self.helpers = HelpersMbs(driver)

    def navigation_to_activities_page(self):
        url = "http://localhost:4200/activities"
        self.helpers.navigation_to_base_url(url)

