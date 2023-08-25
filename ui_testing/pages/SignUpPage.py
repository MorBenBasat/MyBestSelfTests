from locators.SignUpLocators import SignUpLocators
from waits.wait import wait_for_element_presence, wait_for_element_visibility, wait_for_element_clickable


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver

    def create_register(self, firstname, lastname, email, username, gender, password, confirm_password):
        click_to_sign_up = wait_for_element_visibility(self.driver,*SignUpLocators.CREATE_NEW_USER)
        click_to_sign_up.click()
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
            print("זכר נבחר")
        elif gender == 'נקבה':
            gender_selection_female.click()
            print("נקבה נבחרה")

        else:
            raise Exception("no gender as been selected")

        password_input = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_PASSWORD)
        password_input.send_keys(password)

        confirm_password_input = wait_for_element_visibility(self.driver, *SignUpLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password_input.send_keys(confirm_password)

        click_to_create = wait_for_element_clickable(self.driver,*SignUpLocators.REGISTER_CREATE_BTN)
        click_to_create.click()


