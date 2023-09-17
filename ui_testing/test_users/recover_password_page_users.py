
class TestRecoverPasswordUsers:

    def __init__(self, email):
        self.email = email


ValidEmail = TestRecoverPasswordUsers("test123@gmail.com")
InvalidEmail = TestRecoverPasswordUsers("testtest")
NoEmail = TestRecoverPasswordUsers("")
