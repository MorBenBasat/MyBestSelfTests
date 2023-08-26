import time
from waits import wait

from selenium.webdriver.common.by import By


class HelpersMbs:
    def __init__(self, driver):
        self.driver = driver

    def navigation_to_base_url(self, url):
        self.driver.get(url)

    def alerts_for_login(self):
        red_alert = wait.wait_for_element_visibility(self.driver, By.XPATH,
                                                     '/html/body/app-root/div/p-toast/div/p-toastitem/div/div')
        green_alert = wait.wait_for_element_visibility(self.driver, By.XPATH,
                                                       '/html/body/app-root/div/p-toast/div/p-toastitem/div/div')
        if green_alert.is_displayed():
            verify_green_msg = green_alert.text
            print('green msg display', verify_green_msg)

        elif red_alert.is_displayed():
            verify_error_msg = red_alert.text
            print('error connect system', verify_error_msg)


    def alerts_for_regirster(self):
        red_alert = wait.wait_for_element_visibility(self.driver, By.XPATH,
                                                     '/html/body/app-root/div/p-toast/div/p-toastitem/div/div')
        green_alert = wait.wait_for_element_visibility(self.driver, By.XPATH,
                                                       '/html/body/app-root/div/p-toast/div/p-toastitem/div/div')
        if green_alert.is_displayed():
            verify_green_msg = green_alert.text
            print('green msg display', verify_green_msg)

        elif red_alert.is_displayed():
            verify_error_msg = red_alert.text
            print('error connect system', verify_error_msg)


