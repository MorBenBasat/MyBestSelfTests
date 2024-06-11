from helpers.Helpers import HelpersMbs


class TestRegisterUsers:
    def __init__(self, firstname, lastname, email, username, gender, password, confirm_password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.gender = gender
        self.password = password
        self.confirm_password = confirm_password


# Example usage:
ValidRegistrationUser = TestRegisterUsers("first name", "lastname", "validemail@gmail.com",
                                          HelpersMbs.random_username(),
                                          "נקבה", "123456test", "123456test")
InvalidRegistrationUser = TestRegisterUsers("first", "last", "Invalidate", "asd1231", "זכר",
                                            "123436test", "123456")
NoPasswordRegistration = TestRegisterUsers("first", "last", "test@gmail.com", HelpersMbs.random_username(), "זכר", "",
                                           "123456")
DifferentPasswordAndConfirm = TestRegisterUsers("first", "last", "test@gmail.com", HelpersMbs.random_username(), "זכר",
                                                "123123test", "123456test")
FemaleRadioSelection = TestRegisterUsers("female", "female", "validemail@gmail.com", HelpersMbs.random_username(),
                                         "נקבה",
                                         "123456test", "123456test")

NoFirstNameRegistration = TestRegisterUsers("", "last", "test@gmail.com", HelpersMbs.random_username(), "זכר",
                                            "123123test", "123456test")
NoLastNameRegistration = TestRegisterUsers("first", "", "test@gmail.com", HelpersMbs.random_username(), "זכר",
                                           "123123test", "123456test")
NoEmailRegistration = TestRegisterUsers("first", "last", "", HelpersMbs.random_username(), "זכר", "123123test",
                                        "123456test")
NoFillRegistrationFields = TestRegisterUsers("", "", "", "", "", "", "")
InvalidLengthUserName = TestRegisterUsers("test123", "258963", "validemail@gmail.com", "testtesttest",
                                          "זכר", "123456test", "123456test")
InvalidLengthPassword = TestRegisterUsers("test123", "258963", "validemail@gmail.com", HelpersMbs.random_username(),
                                          "זכר", "InvalidPasswordLength123", "InvalidPasswordLength123")
FemaleGenderSelection = TestRegisterUsers("test123", "258963", "validemail@gmail.com", HelpersMbs.random_username(),
                                          "נקבה", "123456test", "123456test")
MaleGenderSelection = TestRegisterUsers("test123", "258963", "validemail@gmail.com", HelpersMbs.random_username(), "זכר"
                                        ,
                                        "123456test", "123456test")
ValidRegisterUserExist = TestRegisterUsers("first name", "lastname", "validemail@gmail.com", HelpersMbs.random_username(
                                            ),
                                           "זכר", "123456test", "123456test")
