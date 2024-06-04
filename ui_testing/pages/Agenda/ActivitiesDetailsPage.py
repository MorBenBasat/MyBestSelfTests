from selenium.webdriver import ActionChains, Keys
from helpers.Helpers import HelpersMbs
from locators.agenda_menu_locators.MyAgendaPageLocators import MyAgendaPageLocators
from pages.Agenda.MyAgendaPage import MyAgendaPage
from pages.Pages_url import PagesUrlMbs
from waits.wait import wait_for_element_presence, wait_for_element_clickable, wait_for_element_visibility
from locators.agenda_menu_locators.ActivitiesDetailsLocators import ActivitiesDetailsLocators
from pages.LoginPage import LoginPage


def get_day_button_locator(day):
    day_locators = {
        "ראשון": ActivitiesDetailsLocators.SUNDAY_TEXT,
        "שני": ActivitiesDetailsLocators.MONDAY_TEXT,
        "שלישי": ActivitiesDetailsLocators.TUESDAY_TEXT,
        "רביעי": ActivitiesDetailsLocators.WEDNESDAY_TEXT,
        "חמישי": ActivitiesDetailsLocators.THURSDAY_TEXT,
        "שישי": ActivitiesDetailsLocators.FRIDAY_TEXT,
        "שבת": ActivitiesDetailsLocators.SATURDAY_TEXT
    }
    return day_locators.get(day)


class ActivitiesDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.helpers = HelpersMbs(self.driver)
        self.pageUrl = PagesUrlMbs.activities_details
        self.my_agenda = MyAgendaPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.action_chains = ActionChains(self.driver)

    def navigate_to_activities_details_page(self):
        self.helpers.navigation_to_url(self.pageUrl)

    def navigate_to_activities_details_page_by_drop_list(self):
        agenda_menu = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.AGENDA_MENU)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(agenda_menu).perform()
        HelpersMbs.delay(1)

        click_add_new_activity_detail = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.
                                                                   DROP_LIST_NEW_ACTIVITIES_DETAILS_BTN)
        click_add_new_activity_detail.click()

        HelpersMbs.delay(1)

    def navigate_to_activities_details_page_by_plus_btn(self):
        HelpersMbs.delay(1)
        self.my_agenda.navigate_to_agenda_page()

        click_on_plus_btn = wait_for_element_clickable(self.driver,
                                                       *MyAgendaPageLocators.PLUS_BTN_OPEN_ACTIVITY_DETAILS)
        click_on_plus_btn.click()

    def create_activity_details(self, ActivityDetails):
        self.fill_all_activities_details_without_btn_click(ActivityDetails)
        HelpersMbs.delay(1)
        click_confirm_btn = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.CONFIRM_BTN)
        click_confirm_btn.click()
        HelpersMbs.delay(2)

    def fill_fields_until_time_field(self, ActivityDetails):
        my_activity_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.MY_ACTIVITY)
        my_activity_field.click
        HelpersMbs.delay(2)
        my_activity_field.send_keys(ActivityDetails.activity_name)

        activity_description_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.
                                                               ACTIVITY_DESCRIPTION)
        activity_description_field.send_keys(ActivityDetails.activity_text)

    def fill_fields_until_day_field(self, ActivityDetails):
        my_activity_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.MY_ACTIVITY)
        my_activity_field.click
        HelpersMbs.delay(1)
        my_activity_field.send_keys(ActivityDetails.activity_name)

        activity_description_field = wait_for_element_presence(self.driver,
                                                               *ActivitiesDetailsLocators.ACTIVITY_DESCRIPTION)
        activity_description_field.send_keys(ActivityDetails.activity_text)

        time_field_open = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        time_field_open.click()
        HelpersMbs.delay(1)
        for _ in range(5):
            time_field_open.send_keys(Keys.BACK_SPACE)
        HelpersMbs.delay(1)
        fill_hour_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        fill_hour_field.send_keys(ActivityDetails.hour)

        random_click = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.ACTIVITY_DESCRIPTION)
        random_click.click()
        HelpersMbs.delay(2)

    def select_time_by_arrows(self):
        time_field_open = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        time_field_open.click()
        HelpersMbs.delay(1)

        hour_arrow_up_click = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.HOUR_ARROW_UP)
        hour_arrow_up_click.click()
        HelpersMbs.delay(1)

        hour_arrow_up_click = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.HOUR_ARROW_UP)
        hour_arrow_up_click.click()

        hour_arrow_down_click = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.HOUR_ARROW_DOWN)
        hour_arrow_down_click.click()
        HelpersMbs.delay(1)

        min_arrow_up = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.MIN_ARROW_UP)
        min_arrow_up.click()
        HelpersMbs.delay(1)

        min_arrow_down = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.MIN_ARROW_DOWN)
        min_arrow_down.click()
        HelpersMbs.delay(1)

    def fill_all_activities_details_without_btn_click(self, ActivityDetails):
        my_activity_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.MY_ACTIVITY)
        my_activity_field.click()
        HelpersMbs.delay(1)
        my_activity_field.send_keys(ActivityDetails.activity_name)

        activity_description_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.
                                                               ACTIVITY_DESCRIPTION)
        activity_description_field.send_keys(ActivityDetails.activity_text)

        time_field_open = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        time_field_open.click()
        HelpersMbs.delay(1)
        for _ in range(5):
            time_field_open.send_keys(Keys.BACK_SPACE)
        HelpersMbs.delay(1)
        fill_hour_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        fill_hour_field.send_keys(ActivityDetails.hour)

        random_click = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.ACTIVITY_DESCRIPTION)
        random_click.click()
        HelpersMbs.delay(1)

        # Fill days field only if day is not None
        if ActivityDetails.day is not None:
            days_field_open = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.DAYS_FIELD)
            days_field_open.click()
            HelpersMbs.delay(1)

            days_field_selection = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.DAYS_SEARCH_FIELD)
            days_field_selection.click()
            HelpersMbs.delay(1)

            days_field_selection.send_keys(ActivityDetails.day)

            day_selection = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.SUNDAY_BTN)
            day_selection.click()
            HelpersMbs.delay(1)

            random_click.click()

    def select_day_and_remove(self, ActivityDetails):
        self.fill_all_activities_details_without_btn_click(ActivityDetails)
        click_to_remove_day = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.REMOVE_DAY_SELECTION)
        HelpersMbs.delay(1)
        click_to_remove_day.click()
        HelpersMbs.delay(2)

    def radio_all_days_click(self, ActivityDetails):
        self.fill_fields_until_time_field(ActivityDetails)
        click_open_days_field = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.DAYS_FIELD)
        click_open_days_field.click()
        HelpersMbs.delay(1)
        click_all_days_btn = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.PICK_ALL_DAYS_RADIO_BTN)
        click_all_days_btn.click()
        return wait_for_element_visibility(self.driver, *ActivitiesDetailsLocators.DAYS_FIELD)

    def write_unexist_day_in_day_search(self, expected_message):
        HelpersMbs.delay(2)
        click_open_days_field = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.DAYS_FIELD)
        click_open_days_field.click()
        HelpersMbs.delay(1)
        write_day_in_search_field = wait_for_element_visibility(self.driver,
                                                                *ActivitiesDetailsLocators.DAYS_SEARCH_FIELD)
        write_day_in_search_field.send_keys("not exist")
        HelpersMbs.delay(1)
        alert_message_not_exist = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.NO_FOUND_DAY_ALERT)
        HelpersMbs.delay(1)
        if alert_message_not_exist.text == expected_message:
            print('text is as expected', expected_message)
        else:
            print('Text is not as expected.Actual text:', alert_message_not_exist)
        return alert_message_not_exist.text

    def verify_my_activity_mandatory_text(self, expected_text):
        HelpersMbs.delay(1)
        my_activity_text = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.MY_ACTIVITY_MANDATORY_TEXT)
        HelpersMbs.delay(1)

        if my_activity_text.text == expected_text:
            print('Text is as expected:', expected_text)
        else:
            print('Text is not as expected. Actual text:', my_activity_text.text)
        return my_activity_text.text

    def verify_hour_mandatory_text(self, expected_text):
        time_field_open = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        time_field_open.click()
        HelpersMbs.delay(1)
        for _ in range(5):
            time_field_open.send_keys(Keys.BACK_SPACE)
        HelpersMbs.delay(1)
        random_click = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.MY_ACTIVITY)
        random_click.click()
        my_activity_hour_text = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.
                                                          MY_ACTIVITY_MANDATORY_TEXT)
        HelpersMbs.delay(1)
        if my_activity_hour_text.text == expected_text:
            print('Text is as expected:', expected_text)
        else:
            print('Text is not as expected. Actual text:', my_activity_hour_text.text)
        return my_activity_hour_text.text

    def verify_day_mandatory_text(self, expected_text):
        HelpersMbs.delay(1)
        my_activity_text = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.DAYS_MANDATORY_TEXT)
        HelpersMbs.delay(1)

        if my_activity_text.text == expected_text:
            print('Text is as expected:', expected_text)
        else:
            print('Text is not as expected. Actual text:', my_activity_text.text)
        return my_activity_text.text

    def green_creation_alert(self, ActivityDetails):
        self.create_activity_details(ActivityDetails)
        green_alert_element = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.GREEN_ALERT)
        green_alert_text = green_alert_element.text
        return green_alert_text

    def verify_hour(self):
        time_field = wait_for_element_clickable(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        time_field.click()
        HelpersMbs.delay(2)

        hour_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.HOUR_TEXT)
        hour_field_text = hour_field.text

        min_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.MIN_TEXT)
        min_field_text = min_field.text

        return hour_field_text, min_field_text

    def verify_clear_fields_navigate_drop_list(self):
        activity_name = wait_for_element_visibility(self.driver, *ActivitiesDetailsLocators.MY_ACTIVITY)
        activity_description = wait_for_element_visibility(self.driver, *ActivitiesDetailsLocators.ACTIVITY_DESCRIPTION)
        hour_field = wait_for_element_visibility(self.driver, *ActivitiesDetailsLocators.TIME_FIELD)
        day_field = wait_for_element_visibility(self.driver, *ActivitiesDetailsLocators.DAYS_FIELD)

        activity_name_text = activity_name.text
        activity_description_text = activity_description.text
        hour_text = hour_field.text
        day_field_text = day_field.text

        assert activity_name_text == "", "Activity name field is not clear"
        assert activity_description_text == "", "Activity description field is not clear"
        assert hour_text == "", "Hour field is not clear"
        assert day_field_text == "באיזה ימים זה קורה", "Day field is not showing the default"

        return self.verify_hour()

    def select_day_radio_button(self, day):
        day_button_locator = get_day_button_locator(day)
        days_field = wait_for_element_presence(self.driver, *ActivitiesDetailsLocators.DAYS_FIELD)
        days_field.click()
        if day_button_locator:
            day_button = wait_for_element_clickable(self.driver, *day_button_locator)
            HelpersMbs.delay(1)
            day_button.click()
            HelpersMbs.delay(1)
            print(f"Clicked on {day}")
        else:
            print(f"No locator found for {day}. Please provide a valid day.")
