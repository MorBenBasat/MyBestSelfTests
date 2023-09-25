import time

from waits import wait
from selenium.webdriver.common.by import By


class HelpersMbs:
    def __init__(self, driver):
        self.driver = driver

    def navigation_to_url(self, url):
        self.driver.get(url)
        HelpersMbs.delay(2)

    def alerts_login(self):
        alert = wait.wait_for_element_visibility(self.driver, By.XPATH,
                                                 '/html/body/app-root/div/p-toast/div/p-toastitem/div/div')
        if alert.is_displayed():
            verify_msg = alert.text
            return verify_msg
        else:
            return None

    def alerts_activities_details(self):
        alert = wait.wait_for_element_visibility(self.driver, By.XPATH,
                                                 '/html/body/app-root/div/p-toast/div/p-toastitem/div/div')
        if alert.is_displayed():
            verify_msg = alert.text
            return verify_msg
        else:
            return None

    def alerts_signup(self):
        alert = wait.wait_for_element_visibility(self.driver, By.XPATH,
                                                 '/html/body/app-root/div/p-toast/div/p-toastitem/div/div')
        if alert.is_displayed():
            verify_msg = alert.text
            return verify_msg
        else:
            return None

    def alerts_recover_password(self):
        alert = wait.wait_for_element_visibility(self.driver, By.XPATH,
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
        return "true" in btn.get_attribute("ng-reflect-disabled")

    def is_enabled(self, selector: tuple[str, str]):
        btn = wait.wait_for_element_clickable(self, *selector)
        return btn.is_enabled()

    @staticmethod
    def is_field_valid(driver, selector: tuple[str, str]):
        field = wait.wait_for_element_visibility(driver, *selector)
        return "ng-invalid" not in field.get_attribute("class") or "ng-dirty" not in field.get_attribute("class")
