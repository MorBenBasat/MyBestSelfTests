from selenium.webdriver.common.by import By


class PasswordRecoverPage:
    EMAIL_FIELD = By.ID, 'email'
    CONFIRM_BTN = By.XPATH, '/html/body/app-root/div/div/app-recover-password/div/p-card/div/div/div[' \
                            '2]/div/p-button/button'
