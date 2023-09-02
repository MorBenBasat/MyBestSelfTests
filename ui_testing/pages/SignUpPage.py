import time

from helpers.Helpers import HelpersMbs
from locators.SignUpLocators import SignUpLocators
from pages.LoginPage import LoginPage
from pages.pages_url import PagesUrlMbs
from waits.wait import wait_for_element_presence, wait_for_element_visibility, wait_for_element_clickable


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.pageUrl = PagesUrlMbs.register
        self.loginpage = LoginPage(self.driver)
        self.helpers = HelpersMbs(self.driver)

    def navigate_to_signup_page(self):
        create_user = wait_for_element_visibility(self.driver, *SignUpLocators.CREATE_NEW_USER)
        create_user.click()

    def create_register(self, firstname, lastname, email, username, gender, password, confirm_password):
        name = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_NAME)
        name.send_keys(firstname)

        last_name = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_LASTNAME)
        last_name.send_keys(lastname)

        write_email = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_NAME_EMAIL)
        write_email.send_keys(email)

        user_name = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_USERNAME)
        user_name.send_keys(username)

        gender_selection_male = wait_for_element_visibility(self.driver, *SignUpLocators.GENDER_RADIO_MALE)
        gender_selection_female = wait_for_element_visibility(self.driver, *SignUpLocators.GENDER_RADIO_FEMALE)

        if gender == 'זכר':
            gender_selection_male.click()
        elif gender == 'נקבה':
            gender_selection_female.click()

        else:
            raise Exception("no gender as been selected")

        password_input = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_PASSWORD)
        password_input.send_keys(password)

        confirm_password_input = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password_input.send_keys(confirm_password)

        click_to_create = wait_for_element_clickable(self.driver, *SignUpLocators.REGISTER_CREATE_BTN)
        click_to_create.click()
