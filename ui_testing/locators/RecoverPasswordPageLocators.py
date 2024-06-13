from selenium.webdriver.common.by import By


class RecoverPasswordPageLocators:
    FORGOT_PASSWORD_BTN = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[2]/div/a[1]'
    EMAIL_FIELD = By.XPATH, '/html/body/app-root/div/div/app-recover-password/div/p-card/div/div/div[' \
                            '2]/div/app-form/form/app-input-wrapper/div/app-input-text-field/div/input'
    CONFIRM_BTN = By.XPATH, '/html/body/app-root/div/div/app-recover-password/div/p-card/div/div/div[' \
                            '2]/div/p-button/button'
    ERROR_ALERT = By.XPATH, '/html/body/app-root/div/div/app-recover-password/div/p-card/div/div/div[' \
                            '2]/div/app-form/form/app-input-wrapper/small'
    REGISTER_BTN = By.XPATH, '/html/body/app-root/div/div/app-recover-password/div/p-card/div/div/div[2]/div/a[2]'
    LOGIN_BTN = By.XPATH, '/html/body/app-root/div/div/app-recover-password/div/p-card/div/div/div[2]/div/a[1]'
    MANDATORY_EMAIL_ALERT = By.XPATH, '/html/body/app-root/div/div/app-recover-password/div/p-card/div/div/div[' \
                                      '2]/div/app-form/form/app-input-wrapper/small'
