class TestLoginUsers:
    def __init__(self, login, password):
        self.login = login
        self.password = password


SuccessLoginUser = TestLoginUsers("test", "258963")
InvalidLogin = TestLoginUsers("Invalid", "Invalid")
UserNameInvalidLength = TestLoginUsers("hi", "123456test")
PasswordInvalidLength = TestLoginUsers("TestUserName123", "123")
NoFillDetails = TestLoginUsers("", "")
NoFillUserName = TestLoginUsers("", "123456test")
NoFillPassword = TestLoginUsers("ValidUser", "")
