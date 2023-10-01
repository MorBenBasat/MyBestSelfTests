from selenium.webdriver.common.by import By


class DisconnectSystemLocators:

    DISCONNECT_BTN = By.CSS_SELECTOR, 'a[href="/logout"]'
    LOGO = By.XPATH, '/html/body/app-root/div/div[1]/app-header/p-menubar/div/div[1]/a/img'
