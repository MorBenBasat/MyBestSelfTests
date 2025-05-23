import time
from datetime import datetime, timedelta

from selenium.common import TimeoutException

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
            print("The expected text:", expected_text)
        else:
            print("Unexpected text : ", self)
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
    def scroll_to_bottom_or_up(driver, which_way):
        if which_way == "DOWN":
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        elif which_way == "UP":
            driver.execute_script("window.scrollTo(0, 0);")
        else:
            raise ValueError("Invalid value for 'which_way'. Use 'DOWN' or 'UP'.")

    def is_button_disabled(self, by, locator, timeout=10):
        try:
            # Wait for the button to be present using custom wait function
            button = wait_for_element_presence(self, by, locator, timeout)
            return button.get_attribute('disabled') is not None
        except TimeoutException:
            return False

    @staticmethod
    def get_yesterday_date_in_hebrew(self):
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

        # Get yesterday's date
        yesterday = datetime.now() - timedelta(1)

        # Format the day and year
        day = yesterday.strftime('%d')
        year = yesterday.strftime('%Y')

        # Get the month name in English
        month_name_english = yesterday.strftime('%B')

        # Map the month name to Hebrew
        month_name_hebrew = month_mapping.get(month_name_english, month_name_english)

        # Construct the date string in the desired format
        yesterday_date_hebrew = f"{day} ב{month_name_hebrew} {year}"

        return yesterday_date_hebrew
