import time
from pages.LoginPage import LoginPage, NegativeLogin
from ui_testing.pages.pages_url import MbsUrl


from initialize_driver import initialize_driver

driver = initialize_driver()
driver.maximize_window()
base_url = MbsUrl(driver)
base_url.main_url()

login_system = NegativeLogin(driver)
login_system.invalid_username_valid_password('AAAA','258963')




time.sleep(2)
