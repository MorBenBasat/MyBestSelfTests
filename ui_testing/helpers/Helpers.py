import time
from waits import wait
from selenium.webdriver.common.by import By


class HelpersMbs:
    def __init__(self, driver):
        self.driver = driver

    def navigation_to_url(self, url):
        self.driver.get(url)
        time.sleep(3)

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
