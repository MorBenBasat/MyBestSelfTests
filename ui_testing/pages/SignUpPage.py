from ui_testing.locators.SignUpLocators import SignUpLocators
from ui_testing.pages.pages_url import MbsUrl
from ui_testing.waits.wait import wait_for_element_presence, wait_for_element_visibility, wait_for_element_clickable


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = MbsUrl.main_url(self.driver)

    def create_registrion(self, firstname, lastname, email, username, password, confirm_password):
        name = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_NAME)
        name.send_keys(firstname)

        last_name = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_LASTNAME)
        last_name.send_keys(lastname)

        write_email = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_NAME_EMAIL)
        write_email.send_keys(email)

        user_name = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_USERNAME)
        user_name.send_keys(username)

        



