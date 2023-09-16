import unittest
from pages.Pages_url import PagesUrlMbs
from pages.SignUpPage import SignUpPage
import pytest
from initialize_driver import initialize_driver
from helpers.Helpers import HelpersMbs
from pages.LoginPage import LoginPage
from test_users.register_users import ValidRegistrationUser, NoPasswordRegistration, \
    DifferentPasswordAndConfirm, NoFirstNameRegistration, NoLastNameRegistration, NoEmailRegistration, \
    NoFillRegistrationFields, InvalidLengthUserName, InvalidLengthPassword


class TestSignUp(unittest.TestCase):

    def setUp(self):
        self.driver = initialize_driver()
        self.helpers = HelpersMbs(self.driver)
        self.login_page = LoginPage(self.driver)
        self.signup_page = SignUpPage(self.driver)

    @pytest.mark.test36
    def test_success_navigation_sign_up_page(self):
        self.signup_page.navigate_to_signup_page()
        HelpersMbs.delay(2)
        self.assertEqual(self.driver.current_url, PagesUrlMbs.register, print("Sign Up Page Open"))
        self.driver.quit()

    @pytest.mark.test37
    def test_success_registration(self):
        self.signup_page.navigate_to_signup_page()
        HelpersMbs.delay(2)
        self.signup_page.create_register(ValidRegistrationUser)
        alert = self.helpers.alerts_signup()
        HelpersMbs.delay(2)
        self.assertEqual(alert, 'הרשמה למערכת\nברוך הבא test אנו שמחים שבחרת להצטרך אלינו', 'הוקם משתמש במערכת')
        self.assertEqual(self.driver.current_url, PagesUrlMbs.login, 'נפתח דף כניסה')
        self.login_page.login
        self.assertEqual(self.driver.current_url, PagesUrlMbs.my_profile, "כניסה בוצעה בהצלחה")
        self.helpers.alerts_login()
        self.driver.quit()

    @pytest.mark.test38
    def test_create_user_without_password(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(NoPasswordRegistration)
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצר משתמש')
        self.driver.quit()

    @pytest.mark.test39
    def test_no_fll_signup_fields(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(NoFillRegistrationFields)
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', 'לא נוצר משתמש')
        self.driver.quit()

    @pytest.mark.test40
    def test_different_confirm_and_password(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(DifferentPasswordAndConfirm)
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'הסיסמאות לא תואמות', 'ססמאות לא תואמות')
        self.driver.quit()

    @pytest.mark.test46
    def test_fill_without_first_name_field(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(NoFirstNameRegistration)
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', print('לא נוצר משתמש עקב חוסר שם פרטי'))
        self.driver.quit()

    @pytest.mark.test47
    def test_fill_without_last_name_field(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(NoLastNameRegistration)
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'לא מולאו כל הפרטים', print('לא נוצר עקב חוסר שם משפחה'))
        self.driver.quit()

    @pytest.mark.test48
    def test_invalid_email_input(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(NoEmailRegistration)
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'אימייל לא חוקי', print('לא נוצר משתמש בעקבות כתיבת אימייל לא חוקי'))
        self.driver.quit()

    @pytest.mark.test54
    def test_invalid_username_length(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(InvalidLengthUserName)
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'אימייל לא חוקי', print('לא נוצר משתמש עקב שם משתמש קצר מדי '))
        self.driver.quit()

    def test_invalid_password_length(self):
        self.signup_page.navigate_to_signup_page()
        self.signup_page.create_register(InvalidLengthPassword)
        alert = self.helpers.alerts_signup()
        self.assertEqual(alert, 'אימייל לא חוקי', print('לא נוצר משתמש עקב שם משתמש קצר מדי '))
        self.driver.quit()
