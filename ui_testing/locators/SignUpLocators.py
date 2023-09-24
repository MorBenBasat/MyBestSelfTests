from selenium.webdriver.common.by import By


class SignUpLocators:
    CREATE_NEW_USER = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[2]/div/a[2]'
    REGISTER_NAME = By.XPATH, '//*[@id="firstName"]'
    REGISTER_LASTNAME = By.XPATH, '//*[@id="lastName"]'
    REGISTER_NAME_EMAIL = By.ID, 'email'
    REGISTER_USERNAME = By.ID, 'username'

    GENDER_RADIO_MALE = By.XPATH, "/html/body/app-root/div/div/app-register/div/p-card/div/div/div[" \
                                  "2]/div/app-input-radio-field/div/div/div/div[1]/p-radiobutton/div/div[2]"

    GENDER_RADIO_FEMALE = By.XPATH, '/html/body/app-root/div/div/app-register/div/p-card/div/div/div[' \
                                    '2]/div/app-input-radio-field/div/div/div/div[2]/p-radiobutton/div/div[2]'

    REGISTER_PASSWORD = By.ID, 'password'
    REGISTER_CONFIRM_PASSWORD = By.ID, 'passwordVerify'
    REGISTER_CREATE_BTN = By.XPATH, '/html/body/app-root/div/div/app-register/div/p-card/div/div/div[' \
                                    '2]/div/p-button/button'
    ALREADY_HAVING_USER = By.XPATH, '/html/body/app-root/div/div/app-register/div/p-card/div/div/div[2]/div/a'
    USER_ALREADY_EXIST = By.XPATH, '/p-toastitem/div/div'
