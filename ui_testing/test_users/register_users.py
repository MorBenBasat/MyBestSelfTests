class TestRegisterUsers:
    def __init__(self, firstname, lastname, email, username, gender, password, confirm_password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.gender = gender
        self.password = password
        self.confirm_password = confirm_password


ValidRegistrationUser = TestRegisterUsers("test123", "258963","validemail@gmail.com",'testusername123','זכר','123456test','123456test')
InvalidRegistrationUser = TestRegisterUsers("first", "last","Invalidemail",'test','זכר','123456test','123456')

