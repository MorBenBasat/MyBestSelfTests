import time
from datetime import datetime

from locators.MyProfilePageLocators import MyProfilePageLocators
from locators.agenda_menu_locators.ActivitiesDetailsLocators import ActivitiesDetailsLocators
from waits import wait
from selenium.webdriver.common.by import By
import random
import string

from waits.wait import wait_for_element_clickable, wait_for_element_visibility, wait_for_element_presence


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
    def is_disabled(driver, locator: tuple[str, str]):
        btn = wait.wait_for_element_visibility(driver, *locator)
        return "p-disabled" in btn.get_attribute("class")

    def is_enabled(self, locator: tuple[str, str]):
        btn = wait.wait_for_element_clickable(self, *locator)
        return btn.is_enabled()

    @staticmethod
    def is_field_valid(driver, locator: tuple[str, str]):
        field = wait.wait_for_element_visibility(driver, *locator)
        return "ng-invalid" not in field.get_attribute("class") or "ng-dirty" not in field.get_attribute("class")

    def click_on_logo(self):
        HelpersMbs.delay(1)
        logo_click = wait_for_element_clickable(self.driver, *MyProfilePageLocators.SYSTEM_LOGO)
        logo_click.click()

    def random_string(self=8):
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(self))

    def update_alert_text(self):
        green_alert = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.UPDATE_ALERT)
        update_alert_text = green_alert.text
        return update_alert_text

    def compare_text(self, expected_text):
        if self == expected_text:
            print('Text is as expected:', expected_text)
        else:
            print('Text is not as expected:', self)
        return self

    @staticmethod
    def get_today_date_in_hebrew():
        month_mapping = {
            "January": "ינואר",
            "February": "פברואר",
            "March": "מרץ",
            "April": "אפריל",
            "May": "מאי",
            "June": "יוני",
            "July": "יולי",
            "August": "אוגוסט",
            "September": "ספטמבר",
            "October": "אוקטובר",
            "November": "נובמבר",
            "December": "דצמבר"
        }

        # Get today's date
        today = datetime.now()

        # Format the day and year
        day = today.strftime('%d')
        year = today.strftime('%Y')

        # Get the month name in English
        month_name_english = today.strftime('%B')

        # Map the month name to Hebrew
        month_name_hebrew = month_mapping.get(month_name_english, month_name_english)

        # Construct the date string in the desired format
        today_date_hebrew = f"{day} ב{month_name_hebrew} {year}"

        return today_date_hebrew

    @staticmethod
    def scroll_to_bottom(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")