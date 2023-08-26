import time

from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from pages.pages_url import PagesUrlMbs
from pages.SignUpPage import SignUpPage

from initialize_driver import initialize_driver

driver = initialize_driver()
driver.maximize_window()

base_url = HelpersMbs(driver)
base_url.navigation_to_base_url(PagesUrlMbs.login)
time.sleep(2)

create_user = SignUpPage(driver)
create_user.create_register('mor','ben','mor@gmail.com','e','e','e','e')
time.sleep(2)

base_url.alerts_for_regirster()


