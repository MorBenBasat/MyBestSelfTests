from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGINPAGE_USERNAME = By.XPATH, '//*[@id="username"]'
    LOGINPAGE_PASSWORD = By.XPATH, '//*[@id="password"]'

    LOGINPAGE_BTN = By.XPATH, "//button[contains(span/text(),'כניסה')]"
    FORGOT_PASSWORD_BTN = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[2]/div/a[1]'
    CREATE_USER_BTN = By.XPATH, '/html/body/app-root/div/div/app-login/div/p-card/div/div/div[2]/div/a[2]'
   