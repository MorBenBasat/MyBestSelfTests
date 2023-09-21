from test_users.register_users import TestRegisterUsers, ValidRegistrationUser


class TestLoginUsers:
    def __init__(self, login, password):
        self.login = login
        self.password = password


SuccessLoginUser = TestLoginUsers("ValidUser123", "258963test")
InvalidLogin = TestLoginUsers("Invalid", "Invalid")
UserNameInvalidLength = TestLoginUsers("hi", "123456test")
PasswordInvalidLength = TestLoginUsers("TestUser123", "123")
NoFillDetails = TestLoginUsers("", "")
NoFillUserName = TestLoginUsers("", "Password123")
NoFillPassword = TestLoginUsers("ValidUser", "")
ValidNameInvalidPassword = TestLoginUsers("test123", "123456")
InValidNameValidPassword = TestLoginUsers("asd", "258963test")
CreateAndLogin = TestLoginUsers(ValidRegistrationUser.username, ValidRegistrationUser.password)
InvalidUsernameLength = TestLoginUsers("test", "258963test")
InvalidPasswordLength = TestLoginUsers("Validtest123","123t")
FillInvalidLengthFields = TestLoginUsers("test","1234")
