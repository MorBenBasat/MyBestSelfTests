from locators.RecoverPasswordPageLocators import PasswordRecoverPageLocators
from waits.wait import wait_for_element_visibility, wait_for_element_clickable


class RecoverPasswordPage:

    def __init__(self, driver):
        self.driver = driver

    def navigation_to_recover_page(self):
        click_forgot_password = wait_for_element_clickable(self.driver,
                                                           *PasswordRecoverPageLocators.FORGOT_PASSWORD_BTN)
        click_forgot_password.click()

    def send_email(self, email):
        fill_email = wait_for_element_visibility(self.driver, *PasswordRecoverPageLocators.EMAIL_FIELD)
        fill_email.send_keys(email)

        click_to_send = wait_for_element_visibility(self.driver,*PasswordRecoverPageLocators.CONFIRM_BTN)
        click_to_send.click()


