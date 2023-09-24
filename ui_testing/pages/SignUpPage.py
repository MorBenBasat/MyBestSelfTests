from helpers.Helpers import HelpersMbs
from locators.LoginPageLocators import LoginPageLocators
from locators.SignUpLocators import SignUpLocators
from pages.LoginPage import LoginPage
from waits.wait import wait_for_element_visibility, wait_for_element_clickable, wait_for_element_presence
import random


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)

    def navigate_to_signup_page(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        create_user = wait_for_element_visibility(self.driver, *SignUpLocators.CREATE_NEW_USER)
        create_user.click()
        HelpersMbs.delay(2)

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
        HelpersMbs.delay(2)
        password_input = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_PASSWORD)
        password_input.send_keys(UserRegistration.password)

        confirm_password_input = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password_input.send_keys(UserRegistration.confirm_password)

        click_to_create = wait_for_element_clickable(self.driver, *SignUpLocators.REGISTER_CREATE_BTN)
        click_to_create.click()
        HelpersMbs.delay(2)

    def gender_verify_click_radio_button(self, gender=None):
        HelpersMbs.delay(2)

        if gender is None:
            gender = random.choice(['זכר', 'נקבה'])
        HelpersMbs.delay(1)
        if gender == 'זכר':
            male_button = wait_for_element_clickable(self.driver, *SignUpLocators.GENDER_RADIO_MALE)
            male_button.click()
        elif gender == 'נקבה':
            female_button = wait_for_element_clickable(self.driver, *SignUpLocators.GENDER_RADIO_FEMALE)
            female_button.click()

        HelpersMbs.delay(1)

        female_button = wait_for_element_visibility(self.driver, *SignUpLocators.GENDER_RADIO_FEMALE)
        male_button = wait_for_element_visibility(self.driver, *SignUpLocators.GENDER_RADIO_MALE)

        if female_button.is_selected():
            print("The female radio button is selected.")
            return True  # Return True when female radio button is selected
        elif male_button.is_selected():
            print("The male radio button is selected.")
            return True  # Return True when male radio button is selected
        else:
            print("No gender selected!")
            return False  # Return False when no gender is selected

    def create_and_login(self, UserRegistration):
        self.create_register(UserRegistration)
        HelpersMbs.delay(2)
        login_username_input = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_USERNAME)
        login_username_input.click()
        login_username_input.send_keys(UserRegistration.username)

        login_password_input = wait_for_element_presence(self.driver, *LoginPageLocators.LOGINPAGE_PASSWORD)
        login_password_input.send_keys(UserRegistration.password)

        login_btn = wait_for_element_clickable(self.driver, *LoginPageLocators.LOGINPAGE_BTN)
        HelpersMbs.delay(1)
        login_btn.click()
        HelpersMbs.delay(2)

    def create_user_without_click_btn(self, UserRegistration):
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
        HelpersMbs.delay(2)
        password_input = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_PASSWORD)
        password_input.send_keys(UserRegistration.password)

        confirm_password_input = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password_input.send_keys(UserRegistration.confirm_password)

    def create_with_same_field(self, UserRegistration):
        self.create_register(UserRegistration)
        HelpersMbs.delay(2)
        click_create_user_btn = wait_for_element_visibility(self.driver, *SignUpLocators.CREATE_NEW_USER)
        click_create_user_btn.click()
        self.create_register(UserRegistration)

        already_exist = wait_for_element_visibility(self.driver, *SignUpLocators.USER_ALREADY_EXIST)

        if already_exist.text == "user already exists":
            print("User already exists")
            return "user already exists"  # Return the message for validation in the test case
        else:
            return None
