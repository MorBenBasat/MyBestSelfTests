from helpers.Helpers import HelpersMbs
from locators.SignUpLocators import SignUpLocators
from pages.LoginPage import LoginPage
from waits.wait import wait_for_element_visibility, wait_for_element_clickable


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)

    def navigate_to_signup_page(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        create_user = wait_for_element_visibility(self.driver, *SignUpLocators.CREATE_NEW_USER)
        create_user.click()

    def create_register(self, UserRegistration):
        name = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_NAME)
        name.send_keys(UserRegistration.firstname)

        last_name = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_LASTNAME)
        last_name.send_keys(UserRegistration.lastname)

        write_email = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_NAME_EMAIL)
        write_email.send_keys(UserRegistration.email)

        user_name = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_USERNAME)
        user_name.send_keys(UserRegistration.username)

        gender_selection_male = wait_for_element_visibility(self.driver, *SignUpLocators.GENDER_RADIO_MALE)
        gender_selection_female = wait_for_element_visibility(self.driver, *SignUpLocators.GENDER_RADIO_FEMALE)

        if UserRegistration.gender == 'זכר':
            gender_selection_male.click()
        elif UserRegistration.gender == 'נקבה':
            gender_selection_female.click()

        password_input = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_PASSWORD)
        password_input.send_keys(UserRegistration.password)

        confirm_password_input = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password_input.send_keys(UserRegistration.confirm_password)

        click_to_create = wait_for_element_clickable(self.driver, *SignUpLocators.REGISTER_CREATE_BTN)
        click_to_create.click()
        HelpersMbs.delay(2)
