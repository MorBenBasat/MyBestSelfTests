import time

from locators.MyProfilePageLocators import MyProfilePageLocators
from waits import wait
from selenium.webdriver.common.by import By
import random
import string

from waits.wait import wait_for_element_clickable, wait_for_element_visibility


class HelpersMbs:
    def __init__(self, driver):
        self.driver = driver

    def navigation_to_url(self, url):
        self.driver.get(url)
        HelpersMbs.delay(2)

    def alerts_display(self):
        alert = wait_for_element_visibility(self.driver, By.XPATH,
                                            '/html/body/app-root/div/p-toast/div/p-toastitem/div/div')
        if alert.is_displayed():
            verify_msg = alert.text
            return verify_msg
        else:
            return None

    @staticmethod
    def delay(seconds):
        try:
            seconds = float(seconds)
            if seconds >= 0:
                time.sleep(seconds)
            else:
                print("Input should be a non-negative number of seconds.")
        except ValueError:
            print("Invalid input. Please provide a valid number of seconds.")

    @staticmethod
    def is_disabled(driver, selector: tuple[str, str]):
        btn = wait.wait_for_element_visibility(driver, *selector)
        return "p-disabled" in btn.get_attribute("class")

    def is_enabled(self, selector: tuple[str, str]):
        btn = wait.wait_for_element_clickable(self, *selector)
        return btn.is_enabled()

    @staticmethod
    def is_field_valid(driver, selector: tuple[str, str]):
        field = wait.wait_for_element_visibility(driver, *selector)
        return "ng-invalid" not in field.get_attribute("class") or "ng-dirty" not in field.get_attribute("class")

    def click_on_logo(self):
        HelpersMbs.delay(1)
        logo_click = wait_for_element_clickable(self.driver, *MyProfilePageLocators.SYSTEM_LOGO)
        logo_click.click()

    def random_username(self=8):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(self))
