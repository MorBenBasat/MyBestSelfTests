class TestRegisterUsers:
    def __init__(self, firstname, lastname, email, username, gender, password, confirm_password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.gender = gender
        self.password = password
        self.confirm_password = confirm_password


ValidRegistrationUser = TestRegisterUsers("first name", "lastname", "validemail@gmail.com", "671111222R5o", "זכר",
                                          "123456test", "123456test")
InvalidRegistrationUser = TestRegisterUsers("first", "last", "Invalidemail", "test", "זכר", "123456test", "123456")
NoPasswordRegistration = TestRegisterUsers("first", "last", "test@gmail.com", "test123", "זכר", "", "123456")
DifferentPasswordAndConfirm = TestRegisterUsers("first", "last", "test@gmail.com", "test123", "זכר", "123123test",
                                                "123456test")
FemaleRadioSelection = TestRegisterUsers("female", "female", "validemail@gmail.com", "testusername123", "נקבה",
                                         "123456test", "123456test")

NoFirstNameRegistration = TestRegisterUsers("", "last", "test@gmail.com", "test123", "זכר", "123123test",
                                            "123456test")

NoLastNameRegistration = TestRegisterUsers("first", "", "test@gmail.com", "test123", "זכר", "123123test",
                                           "123456test")

NoEmailRegistration = TestRegisterUsers("first", "last", "", "test123", "זכר", "123123test",
                                        "123456test")
NoFillRegistrationFields = TestRegisterUsers("", "", "", "", "", "", "")
InvalidLengthUserName = TestRegisterUsers("test123", "258963", "validemail@gmail.com", "testusername12", "זכר",
                                          "123456test", "123456test")
InvalidLengthPassword = TestRegisterUsers("test123", "258963", "validemail@gmail.com", "testusername12", "זכר",
                                          "InvalidPasswordLength123", "InvalidPasswordLength123")
FemaleGenderSelection = TestRegisterUsers("test123", "258963", "validemail@gmail.com", "femaleSelection1233", "נקבה",
                                          "123456test", "123456test")
MaleGenderSelection = TestRegisterUsers("test123", "258963", "validemail@gmail.com", "maleSelection1233", "זכר",
                                        "123456test", "123456test")
