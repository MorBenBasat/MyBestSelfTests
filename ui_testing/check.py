import time

from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from pages.Pages_url import PagesUrlMbs
from pages.SignUpPage import SignUpPage

from initialize_driver import initialize_driver

driver = initialize_driver()
driver.maximize_window()

base_url = HelpersMbs(driver)
base_url.navigation_to_base_url(PagesUrlMbs.login)
create_user = LoginPage(driver)
create_user.login('test', '258963')
HelpersMbs.delay(2)

base_url.alerts()
base_url.navigation_to_base_url(PagesUrlMbs.agenda)
HelpersMbs.delay(2)

