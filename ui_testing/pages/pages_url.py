class PagesUrl:
    def __init__(self, login, register, my_profile, agenda):
        self.login = login
        self.register = register
        self.my_profile = my_profile
        self.agenda = agenda


# Creating an object of the Person class
PagesUrlMbs = PagesUrl("http://localhost:4200/login", "http://localhost:4200/register",
                       "http://localhost:4200/my-profile", "http://localhost:4200/agenda")
