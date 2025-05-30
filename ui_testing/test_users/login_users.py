from test_users.register_users import ValidRegistrationUser


class TestLoginUsers:
    def __init__(self, username, password):
        self.username = username
        self.password = password


SuccessLoginUser = TestLoginUsers("morbenbasat", "258963mor")
InvalidLogin = TestLoginUsers("Invalid", "Invalid")
UserNameInvalidLength = TestLoginUsers("test", "123456test")
PasswordInvalidLength = TestLoginUsers("Testr123", "1234")
NoFillDetails = TestLoginUsers("", "")
NoFillUserName = TestLoginUsers("", "Password123")
NoFillPassword = TestLoginUsers("ValidUser", "")
ValidNameInvalidPassword = TestLoginUsers("test12312", "123456")
InValidNameValidPassword = TestLoginUsers("asd", "258963test")
CreateAndLogin = TestLoginUsers(ValidRegistrationUser.username, ValidRegistrationUser.password)
FillInvalidLengthFields = TestLoginUsers("test", "1234")
UserTestForLengthAlert = TestLoginUsers("testuser", "12340")
