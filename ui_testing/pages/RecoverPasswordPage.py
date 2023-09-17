from helpers.Helpers import HelpersMbs
from locators.RecoverPasswordPageLocators import PasswordRecoverPageLocators
from pages.LoginPage import LoginPage
from waits.wait import wait_for_element_visibility, wait_for_element_clickable


class RecoverPasswordPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)

    def navigation_to_recover_password_page(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        click_forgot_password = wait_for_element_clickable(self.driver,
                                                           *PasswordRecoverPageLocators.FORGOT_PASSWORD_BTN)
        click_forgot_password.click()
        HelpersMbs.delay(2)

    def send_email(self, EmailRecoverPassword):
        fill_email = wait_for_element_visibility(self.driver, *PasswordRecoverPageLocators.EMAIL_FIELD)
        fill_email.send_keys(EmailRecoverPassword.email)

        click_to_send = wait_for_element_visibility(self.driver, *PasswordRecoverPageLocators.CONFIRM_BTN)
        click_to_send.click()
        HelpersMbs.delay(3)
