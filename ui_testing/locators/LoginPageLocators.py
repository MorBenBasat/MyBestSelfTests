from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGINPAGE_USERNAME = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[' \
                                   '2]/div/app-form/form/app-input-wrapper[1]/div/app-input-text-field/div/input'
    LOGINPAGE_PASSWORD = By.XPATH, '//*[@id="password"]'
    LOGIN_BTN = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[2]/div/p-button/button'
    FORGOT_PASSWORD_BTN = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[2]/div/a[1]'
    CREATE_USER_BTN = By.CSS_SELECTOR, "button.p-ripple.p-element.p-button.p-component[type='button']"

    USERNAME_FIELD_MANDATORY_TEXT = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[' \
                                              '2]/div/app-form/form/app-input-wrapper[1]/small'
    PASSWORD_FIELD_MANDATORY_TEXT = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[' \
                                              '2]/div/app-form/form/app-input-wrapper[2]/small'

    LENGTH_ALERT = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[' \
                             '2]/div/app-form/form/app-input-wrapper[2]/small'

    TITLE_LOGIN_NAME = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[1]'
    SUCCESS_LOGIN_ALERT = By.XPATH, '/html/body/app-root/div/p-toast/div/p-toastitem/div/div'
