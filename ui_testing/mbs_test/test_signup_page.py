import time
import unittest
from pages.SignUpPage import SignUpPage
import pytest
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from test_users.register_users import InvalidRegistrationUser, ValidRegistrationUser


class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.signup_page = SignUpPage(self.driver)

    @pytest.mark.test36
    def test_success_navigation_sign_up_page(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        HelpersMbs.delay(2)
        url = self.driver.current_url
        self.assertEqual('http://localhost:4200/register', url, print("Sign Up Page Open"))
        self.driver.quit()

    @pytest.mark.test37
    def test_success_registration(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(InvalidRegistrationUser.firstname, ValidRegistrationUser.lastname,
                                         ValidRegistrationUser.email, ValidRegistrationUser.username,
                                         ValidRegistrationUser.username, ValidRegistrationUser.password,
                                         ValidRegistrationUser.confirm_password)
        alert = self.helpers.alerts_signup()
        HelpersMbs.delay(2)
        self.assertEqual(alert, 'הרשמה למערכת\nברוך הבא test אנו שמחים שבחרת להצטרך אלינו', 'הוקם משתמש במערכת')
        url = 'http://localhost:4200/login'
        self.assertEqual(url, self.driver.current_url, 'נפתח דף כניסה')
        self.login_page.login('45445888', '111111')
        self.assertEqual(self.driver.current_url, url, "כניסה בוצעה בהצלחה")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test38
    def test_create_user_without_password(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register('first', 'last', 'email', 'username', 'נקבה', '', '123456test')
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצר משתמש')
        self.driver.quit()

    @pytest.mark.test39
    def test_no_fll_signup_fields(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register('', '', '', '', '', '', '')
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצר משתמש')
        self.driver.quit()

    @pytest.mark.test40
    def test_different_confirm_and_password(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register('firstname', 'lastname', 'email@gmail.com', 'username', 'נקבה', '123456test',
                                         '123456')
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'הסיסמאות לא תואמות', 'ססמאות לא תואמות')
        self.driver.quit()

    @pytest.mark.test46
    def test_fill_without_first_name_field(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register('', 'lastname', 'email@gmail.com', 'username', 'נקבה', '123456test',
                                         '123456test')
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצר משתמש')
        self.driver.quit()

    @pytest.mark.test47
    def test_fill_without_last_name_field(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register('firstname', '', 'email@gmail.com', 'username', 'נקבה', '123456test',
                                         '123456test')
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצר משתמש')
        self.driver.quit()

    @pytest.mark.test48
    def test_invalid_email_input(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register('firstname', 'lastname', 'email@', 'username', 'נקבה', '123456test',
                                         '123456test')
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'אימייל לא חוקי', print('לא נוצר משתמש בעקבות כתיבת אימייל לא חוקי'))
        self.driver.quit()

    @pytest.mark.test54
    def test_invalid_username_length(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register('first', 'last', 'email', 'user', 'נקבה', '123456test', '123456test')
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'אימייל לא חוקי', print('לא נוצר משתמש עקב שם משתמש קצר מדי '))
        self.driver.quit()

    def test_invalid_password_length(self):
        self.driver.maximize_window()
        self.login_page.navigate_to_login_page()
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register('first', 'last', 'email', 'user', 'נקבה', '123456test', '123456test')
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'אימייל לא חוקי', print('לא נוצר משתמש עקב שם משתמש קצר מדי '))
        self.driver.quit()
