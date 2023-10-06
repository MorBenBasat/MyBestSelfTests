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
        self.send_email_without_click_btn(EmailRecoverPassword)

        click_to_send = wait_for_element_visibility(self.driver, *PasswordRecoverPageLocators.CONFIRM_BTN)
        click_to_send.click()
        HelpersMbs.delay(2)

    def send_email_without_click_btn(self, EmailRecoverPassword):
        fill_email = wait_for_element_visibility(self.driver, *PasswordRecoverPageLocators.EMAIL_FIELD)
        fill_email.send_keys(EmailRecoverPassword.email)
        HelpersMbs.delay(1)

    def invalid_email_login(self, EmailRecoverPassword):
        self.send_email_without_click_btn(EmailRecoverPassword)
        invalid_email = wait_for_element_visibility(self.driver, *PasswordRecoverPageLocators.ERROR_ALERT)
        if invalid_email.text == "נא להזין מייל חוקי":
            print("מופיע נא להזין מייל חוקי")
            return "נא להזין מייל חוקי"
        else:
            print("Unexpected message:", invalid_email.text)
            return None

    def click_register_btn(self):
        self.navigation_to_recover_password_page()
        register_btn = wait_for_element_clickable(self.driver, *PasswordRecoverPageLocators.REGISTER_BTN)
        register_btn.click()
        HelpersMbs.delay(1)

    def click_login_btn(self):
        self.navigation_to_recover_password_page()
        login_btn = wait_for_element_clickable(self.driver, *PasswordRecoverPageLocators.LOGIN_BTN)
        login_btn.click()
        HelpersMbs.delay(1)
